# -*- coding: utf-8 -*-
"""Generate the static site from data.py.   Usage:  python3 build.py"""
import html, json, os, re
from collections import OrderedDict
from data import SITE, TOPICS, PUBLICATIONS

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = SITE["base_url"].rstrip("/")
NAME = SITE["name"]
OA = {"oa": ("oa-oa", "Free to read on the publisher's website", "Open access"),
      "green": ("oa-green", "A free version is available, e.g. in a repository; the publisher's version needs a subscription", "Free copy available")}

e = html.escape


def bold_me(authors):
    return re.sub(r"\bLee, S\.", "<b>Lee, S.</b>", e(authors, quote=False))


def short_ref(p):
    """'Title. Journal, 12(3), 1-10.' as on the reference site."""
    s = f"{p['title']}. {p['journal']}"
    if p["volume"]:
        s += f", {p['volume']}" + (f"({p['issue']})" if p["issue"] else "")
    if p["pages"]:
        s += f", {p['pages']}"
    return e(s + ".", quote=False)


def apa(p):
    s = f"{bold_me(p['authors'])} ({p['year']}). {e(p['title'], quote=False)}. <i>{e(p['journal'])}</i>"
    if p["volume"]:
        s += f", <i>{e(p['volume'])}</i>" + (f"({e(p['issue'])})" if p["issue"] else "")
    if p["pages"]:
        s += (", Article " if p.get("article") else ", ") + e(p["pages"])
    s += "."
    if p["doi"]:
        u = f"https://doi.org/{p['doi']}"
        s += f' <a href="{u}">{u}</a>'
    return s


def badge(p):
    if p["oa"] in OA:
        cls, tip, label = OA[p["oa"]]
        return f' <span class="oa {cls}" title="{e(tip)}">{label}</span>'
    return ""


def link(p, prefix=""):
    return f"{prefix}papers/{p['slug']}.html"


def page(title, desc, path, body, prefix="", head_extra=""):
    cv = f'<a href="{prefix}{SITE["cv_file"]}">CV</a>' if SITE.get("cv_file") else ""
    prof = " · ".join(f'<a href="{u}">{e(n)}</a>' for n, u in SITE["profiles"] if u)
    foot_links = " · ".join(x for x in [f'<a href="mailto:{SITE["email"]}">Email</a>', prof] if x)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{BASE}/{path}">
<link rel="stylesheet" href="{prefix}style.css">
{head_extra}</head>
<body>
<header class="site"><div class="in"><a class="brand" href="{prefix}index.html">{e(NAME)}</a>
<nav><a href="{prefix}index.html">About</a><a href="{prefix}publications.html">Publications</a>{cv}</nav></div></header>
<main>
{body}
</main>
<footer><div class="in">{e(NAME)} · {e(SITE['title'])}, {e(SITE['affiliation'])}, {e(SITE['institution'])}.<br>{foot_links}</div></footer>
</body>
</html>
"""


def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>\n'


def person():
    return {"@type": "Person", "@id": f"{BASE}/#person", "name": NAME, "jobTitle": SITE["title"],
            "affiliation": {"@type": "Organization", "name": f"{SITE['affiliation']}, {SITE['institution']}",
                            "url": SITE["institution_url"]},
            "knowsAbout": SITE["knows_about"], "url": f"{BASE}/",
            "sameAs": [u for _, u in SITE["profiles"] if u]}


def feat_item(p, prefix=""):
    extra = " · <b>Summary</b>" if p.get("summary") else ""
    return (f'<li><a href="{link(p, prefix)}">{short_ref(p)}</a>{badge(p)}<br>'
            f'<span class="small">{bold_me(p["authors"])} ({p["year"]}){extra}</span></li>')


def build_index():
    pubs = sorted(PUBLICATIONS, key=lambda p: -p["year"])
    prof = " · ".join(f'<a href="{u}">{e(n)}</a>' for n, u in SITE["profiles"] if u)
    contact = f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>'
    if SITE.get("cv_file"):
        contact += f' · <a href="{SITE["cv_file"]}">Curriculum vitae (PDF)</a>'
    if prof:
        contact += " · " + prof
    out = [f"<h1>{e(NAME)}</h1>",
           f'<p class="meta">{e(SITE["title"])} · {e(SITE["affiliation"])}, {e(SITE["institution"])}</p>',
           f"<p>{SITE['bio']}</p>",
           f'<p class="profiles"><b>Contact and profiles:</b> {contact}</p>']
    if SITE.get("honour"):
        out.append(f'<p class="honour">{e(SITE["honour"])}</p>')
    out.append('<p><a href="publications.html"><b>Full list of publications, listed by year</b></a> '
               "(peer-reviewed journal articles and conference presentations). Below, the same publications are grouped "
               'by topic; a paper can appear under more than one. <span class="oa oa-oa">Open access</span> means free '
               'to read on the publisher\'s website; <span class="oa oa-green">Free copy available</span> means a free '
               "version exists elsewhere, for example in a university repository.</p>")
    sections = OrderedDict()
    for sec, tid, label in TOPICS:
        sections.setdefault(sec, []).append((tid, label))
    for sec, items in sections.items():
        out.append(f"<h2>{e(sec)}</h2>")
        for tid, label in items:
            ps = [p for p in pubs if tid in p["topics"]]
            if not ps:
                continue
            out.append(f'<details><summary>{e(label)} <span class="count">({len(ps)})</span></summary><ul class="feat">')
            out += [feat_item(p) for p in ps]
            out.append("</ul></details>")
    desc = f"{NAME}, {SITE['title']} at {SITE['institution']}: " + ", ".join(SITE["knows_about"][:5]) + "."
    head = ld({"@context": "https://schema.org", "@type": "ProfilePage", "url": f"{BASE}/", "mainEntity": person()})
    return page(f"{NAME} – {SITE['tagline']}", desc, "", "\n".join(out), head_extra=head)


def build_publications():
    pubs = sorted(PUBLICATIONS, key=lambda p: -p["year"])
    out = ["<h1>Publications</h1>",
           f'<p class="meta">Peer-reviewed journal articles by {e(NAME)}, most recent first. '
           f'Each title opens a page with the full reference.</p>', "<h2>Journal articles</h2>",
           '<ol class="pubs" reversed>']
    for p in pubs:
        doi = f' <a href="https://doi.org/{p["doi"]}">doi:{e(p["doi"])}</a>' if p["doi"] else ""
        out.append(f'<li>{bold_me(p["authors"])} ({p["year"]}). <a href="{link(p)}">{e(p["title"], quote=False)}</a>. '
                   f'<i>{e(p["journal"])}</i>{(", " + e(p["volume"])) if p["volume"] else ""}'
                   f'{("(" + e(p["issue"]) + ")") if p["issue"] else ""}{(", " + e(p["pages"])) if p["pages"] else ""}.'
                   f"{doi}{badge(p)}</li>")
    out.append("</ol>")
    try:
        from data import PRESENTATIONS
    except ImportError:
        PRESENTATIONS = []
    if PRESENTATIONS:
        out += ["<h2>Conference presentations</h2>", '<ul class="feat">']
        out += [f'<li>{bold_me(a)} ({e(d)}). {e(t, quote=False)}.<br><span class="small">{e(v)}</span></li>'
                for a, d, t, v in PRESENTATIONS]
        out.append("</ul>")
    head = ld({"@context": "https://schema.org", "@type": "CollectionPage", "name": f"Publications of {NAME}",
               "url": f"{BASE}/publications.html", "about": {"@id": f"{BASE}/#person"},
               "hasPart": [{"@type": "ScholarlyArticle", "name": p["title"],
                            **({"sameAs": f"https://doi.org/{p['doi']}"} if p["doi"] else {})} for p in pubs]})
    return page(f"Publications – {NAME}", f"Complete list of peer-reviewed publications by {NAME}.",
                "publications.html", "\n".join(out), head_extra=head)


def cite_name(a):
    """'Kuo, L.-J.' -> 'L.-J. Kuo' for citation_author meta tags."""
    last, _, first = a.partition(", ")
    return f"{first.replace(' ', '')} {last}".strip()


def build_paper(p):
    authors = [x.strip() for x in re.split(r",\s*(?=[A-Z][^,]*,\s*[A-Z]\.)|,?\s*&\s*", p["authors"]) if x.strip()]
    names = [cite_name(a) for a in authors]
    url = f"{BASE}/{link(p)}"
    meta = [f'<meta name="citation_title" content="{e(p["title"])}">']
    meta += [f'<meta name="citation_author" content="{e(n)}">' for n in names]
    meta += [f'<meta name="citation_publication_date" content="{p["year"]}">',
             f'<meta name="citation_journal_title" content="{e(p["journal"])}">']
    if p["volume"]:
        meta.append(f'<meta name="citation_volume" content="{e(p["volume"])}">')
    if p["issue"]:
        meta.append(f'<meta name="citation_issue" content="{e(p["issue"])}">')
    if p["pages"]:
        fp, _, lp = p["pages"].partition("-")
        meta.append(f'<meta name="citation_firstpage" content="{e(fp)}">')
        if lp:
            meta.append(f'<meta name="citation_lastpage" content="{e(lp)}">')
    if p["doi"]:
        meta.append(f'<meta name="citation_doi" content="{e(p["doi"])}">')
    if p.get("keywords"):
        meta.append(f'<meta name="citation_keywords" content="{e("; ".join(p["keywords"]))}">')
    art = {"@context": "https://schema.org", "@type": "ScholarlyArticle", "@id": url, "name": p["title"],
           "author": [{"@type": "Person", "name": n} for n in names], "datePublished": str(p["year"]),
           "isPartOf": {"@type": "Periodical", "name": p["journal"]}, "url": url, "inLanguage": "en"}
    if p.get("summary"):
        art["description"] = p["summary"]
    if p.get("keywords"):
        art["keywords"] = p["keywords"]
    if p["doi"]:
        art["sameAs"] = f"https://doi.org/{p['doi']}"
    head = "\n".join(meta) + "\n" + ld(art)

    doi = f' · DOI <a href="https://doi.org/{p["doi"]}">{e(p["doi"])}</a>' if p["doi"] else ""
    body = ["<article>", f"<h1>{e(p['title'], quote=False)}</h1>",
            f'<p class="meta">{e(", ".join(names))}<br><i>{e(p["journal"])}</i> · {p["year"]}{doi}{badge(p)}</p>']
    if p.get("summary"):
        body += ["<h3>Summary</h3>", f'<p class="summary">{e(p["summary"], quote=False)}</p>']
    if p.get("keywords"):
        body += ["<h3>Keywords</h3>", '<ul class="kw">' + "".join(f"<li>{e(k)}</li>" for k in p["keywords"]) + "</ul>"]
    if p["doi"]:
        body.append(f'<a class="btn" href="https://doi.org/{p["doi"]}">Read the published article →</a>')
    body += ["<h3>How to cite (APA 7th edition)</h3>", f'<p class="cite">{apa(p)}</p>', "</article>"]
    desc = p.get("summary") or f"{p['title']} ({p['journal']}, {p['year']})."
    return page(f"{p['title']} – {NAME}", desc[:300], link(p), "\n".join(body), prefix="../", head_extra=head)


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write("index.html", build_index())
    write("publications.html", build_publications())
    for p in PUBLICATIONS:
        write(link(p), build_paper(p))
    urls = ["", "publications.html"] + [link(p) for p in PUBLICATIONS]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"<url><loc>{BASE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    write(".nojekyll", "")
    print(f"Built {len(PUBLICATIONS)} paper pages + index, publications, sitemap.")


if __name__ == "__main__":
    main()
