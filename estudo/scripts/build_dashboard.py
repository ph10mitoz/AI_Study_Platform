"""Generates a static, offline dashboard from CONTENT_LIBRARY.md.

Read-only: lets you browse/filter the source catalog in a browser instead of
raw markdown. No server, no write-back — open estudo/dashboard/index.html
directly in a browser.
"""

import html
import json
import re
from pathlib import Path

LIBRARY_FILE = Path(__file__).resolve().parent.parent / "CONTENT_LIBRARY.md"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "dashboard" / "index.html"

STATUS_RE = re.compile(r"\*\*\[([^\]]+)\]\*\*")


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def inline(text: str) -> str:
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    return text


def render_table(table_lines: list[str]) -> str:
    rows = [[c.strip() for c in line.strip("|").split("|")] for line in table_lines]
    header, body_rows = rows[0], rows[2:]
    out = ["<table><thead><tr>"]
    out += [f"<th>{inline(h)}</th>" for h in header]
    out.append("</tr></thead><tbody>")
    for row in body_rows:
        if not any(c for c in row):
            continue
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def md_to_html(body: str) -> str:
    lines = body.strip("\n").split("\n")
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    i = 0

    def flush_paragraph():
        if paragraph:
            blocks.append(f"<p>{inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    def flush_list():
        if list_items:
            blocks.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in list_items) + "</ul>")
            list_items.clear()

    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            flush_paragraph()
            flush_list()
            i += 1
            continue
        if line.strip().startswith("|"):
            flush_paragraph()
            flush_list()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            blocks.append(render_table(table_lines))
            continue
        if line.strip().startswith("- "):
            flush_paragraph()
            item_text = line.strip()[2:]
            j = i + 1
            while j < len(lines) and lines[j].startswith("  ") and lines[j].strip():
                item_text += " " + lines[j].strip()
                j += 1
            list_items.append(item_text)
            i = j
            continue
        paragraph.append(line.strip())
        i += 1

    flush_paragraph()
    flush_list()
    return "\n".join(blocks)


def classify(status_text: str | None) -> str:
    if status_text is None:
        return "misto"
    t = status_text.upper()
    if "DESCARTADO" in t:
        return "descartado"
    if "NÃO VERIFICADO" in t or "BLOQUEADO" in t:
        return "nao_verificado"
    if "VERIFICADO" in t:
        return "verificado"
    return "misto"


def clean_title(heading: str) -> str:
    title = STATUS_RE.sub("", heading.lstrip("#").strip())
    return re.sub(r"\s{2,}", " ", title).strip(" -")


def parse_source_block(heading: str, body: str, group: str | None) -> dict:
    match = STATUS_RE.search(heading)
    status = match.group(1) if match else None
    return {
        "title": clean_title(heading),
        "group": group,
        "status": status,
        "status_class": classify(status),
        "body_html": md_to_html(body),
    }


def parse_library(text: str) -> tuple[list[dict], str]:
    sections = re.split(r"\n(?=## )", text)[1:]  # drop H1 + legend intro
    sources: list[dict] = []
    crossref_html = ""

    for section in sections:
        lines = section.split("\n")
        heading, rest = lines[0], "\n".join(lines[1:])

        if heading.startswith("## Cruzamento"):
            crossref_html = md_to_html(rest)
            continue

        if heading.startswith("## Syllabi de universidades"):
            for sub in re.split(r"\n(?=### )", rest):
                sub_lines = sub.split("\n")
                if not sub_lines[0].startswith("###"):
                    continue
                sources.append(
                    parse_source_block(sub_lines[0], "\n".join(sub_lines[1:]), "Syllabi de universidades")
                )
            continue

        sources.append(parse_source_block(heading, rest, None))

    return sources, crossref_html


PAGE_TEMPLATE = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fontes de estudo</title>
<style>
  :root {{
    --bg: #f7f7f5; --fg: #1d1d1f; --muted: #6b6b70; --card: #ffffff;
    --border: #e3e3e0; --accent: #3a6ea5;
    --ok-bg: #e6f4ea; --ok-fg: #1e6b34;
    --warn-bg: #fdecea; --warn-fg: #a13b2b;
    --off-bg: #eeeeee; --off-fg: #666666;
    --mixed-bg: #fff6e0; --mixed-fg: #8a6400;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #17181a; --fg: #eaeaec; --muted: #9a9aa0; --card: #1f2023;
      --border: #313236; --accent: #7aa7d9;
      --ok-bg: #163620; --ok-fg: #7fd99a;
      --warn-bg: #3a211e; --warn-fg: #e8a398;
      --off-bg: #2a2a2d; --off-fg: #a0a0a5;
      --mixed-bg: #3a2f10; --mixed-fg: #e8c35e;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--fg);
    font: 15px/1.5 -apple-system, "Segoe UI", Roboto, sans-serif;
  }}
  header {{ padding: 24px 20px 12px; max-width: 980px; margin: 0 auto; }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  .sub {{ color: var(--muted); font-size: 13px; }}
  main {{ max-width: 980px; margin: 0 auto; padding: 0 20px 60px; }}
  .tabs {{ display: flex; gap: 8px; margin: 16px 0; }}
  .tab {{
    padding: 8px 14px; border-radius: 8px; border: 1px solid var(--border);
    background: var(--card); cursor: pointer; font-size: 13px; color: var(--fg);
  }}
  .tab.active {{ background: var(--accent); color: white; border-color: var(--accent); }}
  .controls {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }}
  input[type=search] {{
    flex: 1; min-width: 180px; padding: 8px 12px; border-radius: 8px;
    border: 1px solid var(--border); background: var(--card); color: var(--fg); font-size: 14px;
  }}
  .chip {{
    padding: 6px 10px; border-radius: 999px; border: 1px solid var(--border);
    background: var(--card); font-size: 12px; cursor: pointer; color: var(--muted); user-select: none;
  }}
  .chip.active {{ color: var(--fg); border-color: var(--accent); }}
  .badge {{ font-size: 11px; padding: 2px 8px; border-radius: 999px; font-weight: 600; white-space: nowrap; }}
  .badge.verificado {{ background: var(--ok-bg); color: var(--ok-fg); }}
  .badge.nao_verificado {{ background: var(--warn-bg); color: var(--warn-fg); }}
  .badge.descartado {{ background: var(--off-bg); color: var(--off-fg); }}
  .badge.misto {{ background: var(--mixed-bg); color: var(--mixed-fg); }}
  .card {{
    background: var(--card); border: 1px solid var(--border); border-radius: 12px;
    padding: 16px 18px; margin-bottom: 12px;
  }}
  .card summary {{ cursor: pointer; display: flex; align-items: center; gap: 10px; font-weight: 600; }}
  .card .group {{ font-size: 11px; color: var(--muted); font-weight: 400; }}
  .card-body {{ margin-top: 12px; color: var(--fg); font-size: 14px; }}
  .card-body p {{ margin: 0 0 10px; }}
  .card-body table {{ width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 13px; }}
  .card-body th, .card-body td {{ border: 1px solid var(--border); padding: 6px 8px; text-align: left; vertical-align: top; }}
  .card-body th {{ background: var(--bg); }}
  .card-body code {{ background: var(--bg); padding: 1px 5px; border-radius: 4px; font-size: 12px; }}
  .card-body a {{ color: var(--accent); }}
  .count {{ color: var(--muted); font-size: 13px; margin-bottom: 10px; }}
  #crossref {{ display: none; }}
  #crossref table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  #crossref th, #crossref td {{ border: 1px solid var(--border); padding: 8px; text-align: left; vertical-align: top; }}
  #crossref th {{ background: var(--card); }}
</style>
</head>
<body>
<header>
  <h1>Fontes de estudo</h1>
  <div class="sub">Gerado de <code>CONTENT_LIBRARY.md</code> — leitura, sem edição aqui.</div>
</header>
<main>
  <div class="tabs">
    <div class="tab active" data-tab="sources">Fontes</div>
    <div class="tab" data-tab="crossref">Por estágio</div>
  </div>

  <div id="sources-view">
    <div class="controls">
      <input type="search" id="search" placeholder="Buscar por título ou conteúdo...">
      <span class="chip active" data-status="all">Todas</span>
      <span class="chip" data-status="verificado">Verificado</span>
      <span class="chip" data-status="nao_verificado">Não verificado</span>
      <span class="chip" data-status="misto">Misto</span>
      <span class="chip" data-status="descartado">Descartado</span>
    </div>
    <div class="count" id="count"></div>
    <div id="cards"></div>
  </div>

  <div id="crossref">{crossref_html}</div>
</main>

<script>
const SOURCES = {sources_json};

const cardsEl = document.getElementById('cards');
const countEl = document.getElementById('count');
const searchEl = document.getElementById('search');
let activeStatus = 'all';

function statusLabel(s) {{
  return {{verificado: 'Verificado', nao_verificado: 'Não verificado', misto: 'Misto', descartado: 'Descartado'}}[s] || s;
}}

function render() {{
  const q = searchEl.value.trim().toLowerCase();
  const filtered = SOURCES.filter(s => {{
    if (activeStatus !== 'all' && s.status_class !== activeStatus) return false;
    if (!q) return true;
    return (s.title + ' ' + s.body_html).toLowerCase().includes(q);
  }});
  countEl.textContent = filtered.length + ' de ' + SOURCES.length + ' fontes';
  cardsEl.innerHTML = filtered.map(s => `
    <details class="card">
      <summary>
        <span class="badge ${{s.status_class}}">${{statusLabel(s.status_class)}}</span>
        ${{s.title}}
        ${{s.group ? `<span class="group">· ${{s.group}}</span>` : ''}}
      </summary>
      <div class="card-body">${{s.body_html}}</div>
    </details>
  `).join('');
}}

document.querySelectorAll('.chip').forEach(chip => {{
  chip.addEventListener('click', () => {{
    document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
    activeStatus = chip.dataset.status;
    render();
  }});
}});
searchEl.addEventListener('input', render);

document.querySelectorAll('.tab').forEach(tab => {{
  tab.addEventListener('click', () => {{
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const isSources = tab.dataset.tab === 'sources';
    document.getElementById('sources-view').style.display = isSources ? '' : 'none';
    document.getElementById('crossref').style.display = isSources ? 'none' : '';
  }});
}});

render();
</script>
</body>
</html>
"""


def main() -> None:
    text = LIBRARY_FILE.read_text(encoding="utf-8")
    sources, crossref_html = parse_library(text)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    page = PAGE_TEMPLATE.format(
        sources_json=json.dumps(sources, ensure_ascii=False),
        crossref_html=crossref_html,
    )
    OUTPUT_FILE.write_text(page, encoding="utf-8")
    print(f"{len(sources)} fontes renderizadas em {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
