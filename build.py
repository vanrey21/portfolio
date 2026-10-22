#!/usr/bin/env python3
"""Generates Reyson Angeles' portfolio page (index.html). Run: python3 build.py"""
from html import escape
from pathlib import Path

PROFILE = {
    "name": "Reyson Angeles",
    "role": "GoHighLevel Expert & Automation Specialist",
    "email": "reysonangeles@gmail.com",
    "linkedin": "https://linkedin.com/in/reysonangeles",
    "location": "Mandaluyong City, Philippines",
    "headline": "Your GHL systems, built to run themselves.",
    "intro": ("I design CRM pipelines, multi-step workflows and cross-platform integrations "
              "that remove manual work and keep your leads moving around the clock, "
              "without a VA babysitting it."),
}

STATS = [("16+", "Years in IT and support"), ("GHL", "CRM specialist"), ("US", "Client focus")]

TRACE = [
    ("Trigger", "Missed call detected", "00:00"),
    ("Action", "Lead captured in CRM", "00:01"),
    ("Action", "Text-back SMS sent", "01:48"),
    ("Action", "Pipeline stage updated", "01:49"),
    ("Action", "Task assigned to closer", "01:50"),
]

SERVICES = [
    ("GoHighLevel build-out",
     "Full GHL setup from scratch: sub-accounts, CRM pipelines, contacts, calendars, booking, funnels and snapshot deployment.",
     ["Pipelines", "Funnels", "Snapshots", "Calendars"]),
    ("Workflow automation",
     "Multi-step workflows that fire on missed calls, form fills, stage changes and bookings. Text-back, nurture, reminders and onboarding.",
     ["Workflows", "SMS / Email", "Triggers", "Sequences"]),
    ("Cross-platform integration",
     "GHL connected to Zapier, Make.com, n8n, Google Sheets, Calendly, Stripe and Slack. Clean data, correct webhooks, no duplicate contacts.",
     ["Zapier", "Make.com", "n8n", "Webhooks"]),
    ("AI-driven automation",
     "OpenAI-powered flows that handle intake, qualify leads, draft replies and route contacts so your team can focus on closing.",
     ["OpenAI", "Lead qualifying", "Auto-response", "Routing"]),
    ("Technical support",
     "Level 2 support for GHL, Zapier and automation stacks. Workflow errors, integration failures and webhook debugging, fixed and documented.",
     ["L2 support", "Root cause", "Debugging", "SOPs"]),
    ("GHL audit and optimization",
     "A full review of your account: broken workflows, redundant automations, missed touchpoints and pipeline gaps, then a rebuilt system that fits your sales team.",
     ["Account audit", "Pipeline fixes", "Tracking", "Documentation"]),
]

CASES = [
    {"client": "GoHighLevel · US client · Disruptive Marketing LLC",
     "title": "Full GHL ecosystem build",
     "body": ("Built complete GoHighLevel infrastructures for multiple US clients: sub-accounts, multi-stage CRM "
              "pipelines, SMS and email nurture, booking calendars and lead routing shaped around each sales process. "
              "Missed-call text-back brought response time under 2 minutes."),
     "tags": ["GoHighLevel", "CRM pipelines", "SMS / Email", "Calendars"],
     "panel": [("CRM pipelines", ""), ("SMS sequences", ""), ("Booking system", ""), ("Lead routing", "")],
     "label": "Ecosystem"},
    {"client": "Automation · Multi-client · Precision Pace",
     "title": "Cross-platform integration systems",
     "body": ("Designed multi-app frameworks with Zapier, Make.com, n8n and webhooks, connecting GHL to Stripe, "
              "Calendly, Google Sheets, Slack and third-party CRMs. Manual entry gone, data flows both ways, "
              "and every integration has error-handling failsafes."),
     "tags": ["Zapier", "Make.com", "n8n", "Webhooks", "API"],
     "panel": [("GoHighLevel → Zapier", "Sheets"), ("Webhook → Make.com", "Stripe"), ("n8n → OpenAI", "GHL")],
     "label": "Integration hub"},
    {"client": "AI automation · Precision Pace",
     "title": "Intelligent VA replacement system",
     "body": ("Built AI-driven systems that replaced manual virtual-assistant work across client accounts: lead intake, "
              "auto-qualification, reply drafting, task assignment and CRM updates, with monitoring and failsafes "
              "for 24/7 reliability."),
     "tags": ["n8n", "OpenAI", "GoHighLevel", "Make.com"],
     "panel": [("Manual follow-ups", "Eliminated"), ("Data entry tasks", "Eliminated"),
               ("Lead response time", "< 2 min"), ("System uptime", "99.9%")],
     "label": "VA replacement"},
    {"client": "Technical support · Infinity Support (Zapier)",
     "title": "Enterprise Zapier support and automation",
     "body": ("Level 2 support for Zapier's enterprise users: diagnosing multi-app workflow failures, rebuilding broken "
              "Zaps, configuring integrations across CRMs, PM tools and chat, and tracing root causes. Also wrote clear "
              "reproduction steps for product bugs sent to engineering."),
     "tags": ["Zapier", "L2 support", "CRM integration", "Root cause analysis"],
     "panel": [("Root cause analysis", "Workflow failures"), ("Multi-app Zap debugging", "Rebuild"),
               ("SOP documentation", "Knowledge base")],
     "label": "Zapier support"},
    {"client": "IT infrastructure · Enterprise support",
     "title": "Enterprise IT administration",
     "body": ("Nine years of enterprise IT support at Alorica and PCCW: Active Directory, Windows Server, Microsoft "
              "Exchange, VMware, Hyper-V, Nutanix and LAN/WAN administration. Handled Level 2 escalations for IT "
              "administrators and server operations at scale."),
     "tags": ["Active Directory", "VMware", "Exchange", "Nutanix"],
     "panel": [("Active Directory", ""), ("Windows Server", ""), ("VMware / Hyper-V", ""),
               ("Exchange Server", ""), ("LAN / WAN", ""), ("PostgreSQL", "")],
     "label": "Infrastructure"},
    {"client": "Operations · Body Science Marketing Group LLC",
     "title": "E-commerce operations management",
     "body": ("Managed order fulfillment across Amazon and Shopify for a multi-client portfolio of health, supplement "
              "and beauty brands: order accuracy, shipping coordination, customer service escalations and social "
              "community management, as a remote operations team of one."),
     "tags": ["Amazon Seller Central", "Shopify", "Order management", "Social media"],
     "panel": [("Platforms", "Amazon + Shopify"), ("Vertical", "Health and beauty"),
               ("Duration", "2.5 years"), ("Scope", "Multi-client")],
     "label": "E-commerce"},
]

PROCESS = [
    ("Discovery and audit", "I map what is manual, broken or missing. For existing GHL accounts that means a full audit of workflow logic, pipeline structure, integration health and contact data."),
    ("System design", "The full architecture is drawn before anything is built: triggers, branching logic, integration touchpoints and failsafes. You see the blueprint first."),
    ("Build and test", "Workflows and integrations are built in staging and tested against every trigger, error state and edge case before they touch live contacts."),
    ("Deploy and document", "After launch I monitor for 48 to 72 hours, then hand over SOPs and a knowledge base so your team can run the system without me."),
]

WHY = [
    ("Infrastructure-level thinking", "Sixteen years of enterprise IT means I know what happens under the interface. Workflows handle edge cases, errors and failures, not just the happy path."),
    ("Documentation first", "Every system ships with SOPs. A new hire should be able to understand and manage it on day one."),
    ("US clients, remote native", "More than ten years serving US-based clients remotely. Async updates, fast turnaround, and overlap with your time zone when it matters."),
    ("AI-augmented, not AI-dependent", "AI tools help me build faster. The architecture, logic and quality control stay with me."),
]

WHY_STATS = [("16+ years", "IT, technical support and automation across enterprise and remote client work"),
             ("< 2 min", "Lead response time through missed-call text-back"),
             ("0 VA tasks", "Manual tasks left after an automation rollout"),
             ("L2", "Enterprise support for Zapier, Good Technology, AT&T and global IT teams")]

STACK = ["GoHighLevel", "Zapier", "n8n", "Make.com", "OpenAI", "Airtable", "Active Directory", "Zendesk"]

CSS = r"""
:root{
  /* Layout: sticky bar, split hero with a live workflow trace, ruled case-file list, one raised proof panel. Dark only. */
  --bg:#070D0F; --surface:#0F181B; --fg:#E8EFED; --muted:#93A4A1; --line:#1F2F32;
  --accent:#8EA2FF; --accent-fg:#071016; --accent-soft:#18214A; --ok:#5ED394;
  --panel:#101D21; --panel-fg:#EAF0EE; --panel-muted:#9FB0AC; --panel-line:#2B4044;
  --display:'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;
  --body:'Instrument Sans','Segoe UI',system-ui,sans-serif;
  --mono:'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace;
  color-scheme:dark;
}

*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:radial-gradient(900px 480px at 78% 0%,color-mix(in srgb,var(--accent) 14%,transparent),transparent 70%) no-repeat,var(--bg);color:var(--fg);font-family:var(--body);font-size:17px;line-height:1.6;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 48px}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:30;background:var(--bg)}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto}
h1,h2,h3{font-family:var(--display);line-height:1.08;margin:0;text-wrap:balance;letter-spacing:-.02em}
p{margin:0}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:4px}

.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--bg);border-bottom:1px solid var(--line)}
.bar .wrap{display:flex;align-items:center;gap:24px;min-height:64px}
.logo{font-family:var(--display);font-weight:800;font-size:1.35rem;text-decoration:none;letter-spacing:-.03em}
.logo span{color:var(--accent)}
.nav{display:flex;gap:26px;margin-left:auto;font-size:.95rem}
.nav a{text-decoration:none;color:var(--muted)}
.nav a:hover{color:var(--fg)}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:6px;font-weight:600;font-size:.95rem;
  text-decoration:none;border:1px solid var(--fg);color:var(--fg);background:transparent;cursor:pointer;font-family:var(--body)}
.btn.primary{box-shadow:0 0 24px color-mix(in srgb,var(--accent) 30%,transparent);background:var(--accent);border-color:var(--accent);color:var(--accent-fg)}
.btn:hover{transform:translateY(-1px)}
.bar .btn{padding:9px 16px}
.bar::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:2px;background:var(--accent);transform:scaleX(0);transform-origin:0 50%}

.hero{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:56px;align-items:center;padding-block:72px 64px}
.avail{display:inline-flex;align-items:center;gap:10px;font-family:var(--mono);font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.dot{width:9px;height:9px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 4px color-mix(in srgb,var(--ok) 25%,transparent)}
.hero h1{font-size:clamp(2.6rem,6.4vw,4.9rem);font-weight:800;margin-block:20px 24px}
.hero h1 em{font-style:normal;color:var(--accent)}
.lede{max-width:56ch;font-size:1.12rem;color:var(--muted)}
.lede strong{color:var(--fg)}
.cta-row{display:flex;flex-wrap:wrap;gap:12px;margin-top:32px}
.stats{display:flex;flex-wrap:wrap;gap:12px 40px;margin-top:44px;padding-top:24px;border-top:1px solid var(--line)}
.stats b{display:block;font-family:var(--display);font-size:2rem;font-weight:800;line-height:1}
.stats span{font-size:.85rem;color:var(--muted)}

.trace{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:20px;font-family:var(--mono);font-size:.84rem;min-width:0}
.trace header{display:flex;justify-content:space-between;gap:12px;color:var(--muted);padding-bottom:14px;border-bottom:1px solid var(--line);font-size:.75rem;letter-spacing:.05em;text-transform:uppercase}
.trace ol{list-style:none;margin:0;padding:8px 0 0}
.trace li{display:grid;grid-template-columns:22px minmax(0,1fr) auto;gap:12px;align-items:start;padding:12px 0;position:relative}
.trace li:not(:last-child)::after{content:"";position:absolute;left:10px;top:34px;bottom:-12px;width:1px;background:var(--line)}
.trace i{width:21px;height:21px;border-radius:50%;border:1.5px solid var(--ok);display:grid;place-items:center;color:var(--ok);font-style:normal;font-size:.7rem}
.trace small{display:block;color:var(--muted);font-size:.7rem;letter-spacing:.06em;text-transform:uppercase}
.trace time{color:var(--muted)}
.trace footer{margin-top:6px;padding-top:14px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:12px;color:var(--ok);flex-wrap:wrap}

section{padding-block:72px;border-top:1px solid var(--line);scroll-margin-top:72px}
.eyebrow{font-family:var(--mono);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
.sec-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px 56px;align-items:end;margin-bottom:44px}
.sec-head h2{font-size:clamp(2rem,4.4vw,3.2rem);font-weight:800;margin-top:12px}
.sec-head h2 em{font-style:normal;color:var(--accent)}
.sec-head p{color:var(--muted);max-width:52ch}

.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:26px;display:flex;flex-direction:column;gap:14px;min-width:0}
.card h3{font-size:1.3rem;font-weight:700}
.card p{color:var(--muted);font-size:.97rem}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:auto;padding-top:6px}
.tag{font-family:var(--mono);font-size:.72rem;padding:4px 9px;border-radius:4px;background:var(--accent-soft);color:var(--accent);white-space:nowrap}

.case{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:48px;padding-block:40px;border-top:1px solid var(--line);align-items:start}
.case:first-of-type{border-top:0;padding-top:0}
.case .client{font-family:var(--mono);font-size:.76rem;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.case h3{font-size:clamp(1.6rem,3vw,2.2rem);font-weight:700;margin-block:10px 14px}
.case p{color:var(--muted);max-width:60ch}
.case .tags{margin-top:20px;padding:0}
.rows{background:var(--surface);border:1px solid var(--line);border-radius:10px;font-family:var(--mono);font-size:.82rem;min-width:0}
.rows h4{margin:0;padding:12px 16px;border-bottom:1px solid var(--line);font-weight:500;font-size:.72rem;letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.rows div{display:flex;justify-content:space-between;gap:16px;padding:12px 16px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.rows div:last-child{border-bottom:0}
.rows span:last-child{color:var(--accent);text-align:right}

.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--surface)}
.step{padding:28px 24px;border-left:1px solid var(--line);display:flex;flex-direction:column;gap:12px;min-width:0}
.step:first-child{border-left:0}
.step b{font-family:var(--mono);font-size:.8rem;color:var(--accent);letter-spacing:.06em}
.step h3{font-size:1.2rem;font-weight:700}
.step p{color:var(--muted);font-size:.95rem}

.proof{background:var(--panel);color:var(--panel-fg);border-radius:14px;padding:clamp(24px,5vw,56px);display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:48px}
.proof h2{font-size:clamp(2rem,4.2vw,3rem);font-weight:800}
.proof h2 em{font-style:normal;color:var(--accent)}
.proof .lead{color:var(--panel-muted);margin-top:20px;max-width:54ch}
.why{display:grid;gap:22px;margin-top:36px}
.why h3{font-size:1.1rem;font-weight:700;font-family:var(--body);letter-spacing:0}
.why p{color:var(--panel-muted);font-size:.95rem;margin-top:4px}
.pstats{display:grid;gap:0;align-content:start}
.pstats div{padding:22px 0;border-bottom:1px solid var(--panel-line)}
.pstats div:first-child{padding-top:0}
.pstats div:last-child{border-bottom:0}
.pstats b{display:block;font-family:var(--display);font-size:2.6rem;font-weight:800;line-height:1;color:var(--panel-fg)}
.pstats span{font-size:.9rem;color:var(--panel-muted)}
.stack{display:flex;flex-wrap:wrap;gap:10px;margin-top:40px}
.stack span{font-family:var(--mono);font-size:.78rem;padding:7px 12px;border:1px solid var(--panel-line);border-radius:5px;color:var(--panel-fg)}
.stack-l{font-family:var(--mono);font-size:.74rem;letter-spacing:.07em;text-transform:uppercase;color:var(--panel-muted);margin-top:36px;display:block}

.contact{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:48px;align-items:center}
.contact h2{font-size:clamp(2.1rem,4.6vw,3.4rem);font-weight:800}
.contact h2 em{font-style:normal;color:var(--accent)}
.contact p.sub{color:var(--muted);margin-top:18px;max-width:50ch}
.mail{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:26px;display:grid;gap:16px;min-width:0}
.mail label{font-family:var(--mono);font-size:.74rem;letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.mail code{display:block;font-family:var(--mono);font-size:1.02rem;padding:14px;border:1px dashed var(--line);border-radius:6px;overflow-wrap:anywhere;user-select:all}
.mail .row{display:flex;flex-wrap:wrap;gap:10px}
.note{font-size:.85rem;color:var(--muted);min-height:1.3em}
footer.site{border-top:1px solid var(--line);padding-top:28px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;font-size:.88rem;color:var(--muted)}

@media (max-width:960px){
  .hero,.case,.proof,.contact,.sec-head{grid-template-columns:minmax(0,1fr)}
  .grid3{grid-template-columns:repeat(2,minmax(0,1fr))}
  .steps{grid-template-columns:repeat(2,minmax(0,1fr))}
  .step:nth-child(3){border-left:0}
  .step:nth-child(n+3){border-top:1px solid var(--line)}
  .hero{padding-block:48px}
}
@media (max-width:640px){
  body{font-size:16px}
  .nav{display:none}
  .bar .btn{margin-left:auto}
  .grid3,.steps{grid-template-columns:minmax(0,1fr)}
  .step{border-left:0;border-top:1px solid var(--line)}
  .step:first-child{border-top:0}
  section{padding-block:52px}
}

/* Scroll-driven motion. Browsers without support just show everything at rest. */
@keyframes rise{from{opacity:0;transform:translateY(56px)}to{opacity:1;transform:none}}
@keyframes from-left{from{opacity:0;transform:translateX(-64px)}to{opacity:1;transform:none}}
@keyframes from-right{from{opacity:0;transform:translateX(64px)}to{opacity:1;transform:none}}
@keyframes drift{from{opacity:1;transform:none}to{opacity:.15;transform:translateY(-90px)}}
@keyframes drift-slow{from{transform:none}to{transform:translateY(60px)}}
@keyframes progress{to{transform:scaleX(1)}}
@supports (animation-timeline:view()){
  .bar::after{animation:progress linear both;animation-timeline:scroll(root)}
  .hero>div:first-child{animation:drift linear both;animation-timeline:scroll(root);animation-range:0 85vh}
  .trace{animation:drift-slow linear both;animation-timeline:scroll(root);animation-range:0 85vh}
  .sec-head,.card,.step,.why>div,.pstats>div,.contact>*,.stack{animation:rise linear both;animation-timeline:view();animation-range:entry 0% entry 45%}
  .case>div:first-child{animation:from-left linear both;animation-timeline:view();animation-range:entry 0% entry 50%}
  .case .rows{animation:from-right linear both;animation-timeline:view();animation-range:entry 0% entry 50%}
}
.js-anim .rv{opacity:0;transform:translateY(56px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.js-anim .rv-l{transform:translateX(-64px)}
.js-anim .rv-r{transform:translateX(64px)}
.js-anim .rv.in{opacity:1;transform:none}
.js-anim .bar::after{transform:scaleX(var(--p,0))}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn:hover{transform:none}*,*::before,*::after{animation:none!important}}
"""

def tags(items):
    return '<div class="tags">' + "".join(f'<span class="tag">{escape(t)}</span>' for t in items) + "</div>"

def build():
    p = PROFILE
    trace = "".join(
        f'<li><i>✓</i><div><small>{escape(k)}</small>{escape(v)}</div><time>{escape(t)}</time></li>'
        for k, v, t in TRACE)
    stats = "".join(f"<div><b>{escape(a)}</b><span>{escape(b)}</span></div>" for a, b in STATS)
    services = "".join(
        f'<article class="card"><h3>{escape(t)}</h3><p>{escape(d)}</p>{tags(tg)}</article>'
        for t, d, tg in SERVICES)
    cases = ""
    for c in CASES:
        rows = "".join(
            f"<div><span>{escape(a)}</span>" + (f"<span>{escape(b)}</span>" if b else "") + "</div>"
            for a, b in c["panel"])
        cases += (f'<article class="case"><div><div class="client">{escape(c["client"])}</div>'
                  f'<h3>{escape(c["title"])}</h3><p>{escape(c["body"])}</p>{tags(c["tags"])}</div>'
                  f'<div class="rows"><h4>{escape(c["label"])}</h4>{rows}</div></article>')
    steps = "".join(
        f'<div class="step"><b>STEP {i+1} OF {len(PROCESS)}</b><h3>{escape(t)}</h3><p>{escape(d)}</p></div>'
        for i, (t, d) in enumerate(PROCESS))
    why = "".join(f"<div><h3>{escape(t)}</h3><p>{escape(d)}</p></div>" for t, d in WHY)
    pst = "".join(f"<div><b>{escape(a)}</b><span>{escape(b)}</span></div>" for a, b in WHY_STATS)
    stack = "".join(f"<span>{escape(s)}</span>" for s in STACK)

    body = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Reyson Angeles</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{escape(p['role'])}. CRM workflows, integrations and AI automation for US clients.">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
</head>
<body>

<header class="bar"><div class="wrap">
  <a class="logo" href="#top">Reyson<span>.</span></a>
  <nav class="nav" aria-label="Sections">
    <a href="#services">Services</a><a href="#portfolio">Portfolio</a><a href="#process">Process</a><a href="#why">Why me</a>
  </nav>
  <a class="btn primary" href="#contact">Work together</a>
</div></header>

<main class="wrap" id="top">
  <div class="hero">
    <div>
      <span class="avail"><span class="dot"></span>Available for new projects</span>
      <h1>Your GHL systems, built to <em>run themselves.</em></h1>
      <p class="lede"><strong>{escape(p['name'])}</strong>, {escape(p['role'])}. {escape(p['intro'])}</p>
      <div class="cta-row">
        <a class="btn primary" href="#portfolio">See my work</a>
        <a class="btn" href="#contact">Get a free audit</a>
      </div>
      <div class="stats">{stats}</div>
    </div>
    <aside class="trace" aria-label="Example automation run">
      <header><span>missed-call-textback</span><span>run #4821</span></header>
      <ol>{trace}</ol>
      <footer><span>● Automation running</span><span>0 manual steps</span></footer>
    </aside>
  </div>

  <section id="services">
    <div class="sec-head">
      <div><span class="eyebrow">What I do</span><h2>GHL expert. <em>Full-stack</em> automation.</h2></div>
      <p>You do not get handed to a junior VA. One senior operator builds, tests, documents and maintains the whole system, start to finish.</p>
    </div>
    <div class="grid3">{services}</div>
  </section>

  <section id="portfolio">
    <div class="sec-head">
      <div><span class="eyebrow">Portfolio</span><h2>Systems I have <em>built and deployed.</em></h2></div>
      <p>Real automations for real clients across CRM, integration, AI, support and operations.</p>
    </div>
    {cases}
  </section>

  <section id="process">
    <div class="sec-head">
      <div><span class="eyebrow">How I work</span><h2>Audit. Build. <em>Automate.</em> Document.</h2></div>
      <p>A tight four-step process that gets your system running quickly and keeps it running reliably.</p>
    </div>
    <div class="steps">{steps}</div>
  </section>

  <section id="why">
    <div class="proof">
      <div>
        <span class="eyebrow">Why Reyson</span>
        <h2 style="margin-top:12px">IT depth. GHL precision. <em>Zero hand-holding.</em></h2>
        <p class="lead">Most GHL specialists learned the platform from tutorials. I came from sixteen years of enterprise IT: Active Directory, server administration and L2 support. I understand systems below the UI, so my automations hold up and my SOPs make sense.</p>
        <div class="why">{why}</div>
      </div>
      <div>
        <div class="pstats">{pst}</div>
        <span class="stack-l">Full tech stack</span>
        <div class="stack" style="margin-top:12px">{stack}</div>
      </div>
    </div>
  </section>

  <section id="contact">
    <div class="contact">
      <div>
        <span class="eyebrow">Let's build</span>
        <h2 style="margin-top:12px">Ready to stop babysitting your <em>automations?</em></h2>
        <p class="sub">Send me a note and I will reply within 24 hours with a free audit of your GHL account, or we start from scratch.</p>
      </div>
      <div class="mail">
        <label for="addr">Email</label>
        <code id="addr">{escape(p['email'])}</code>
        <div class="row">
          <button class="btn primary" id="copy" type="button">Copy email</button>
          <a class="btn" href="mailto:{escape(p['email'])}">Open mail app</a>
          <a class="btn" href="{escape(p['linkedin'])}" target="_blank" rel="noopener">LinkedIn</a>
        </div>
        <p class="note" id="note" role="status"></p>
      </div>
    </div>
  </section>

  <footer class="site">
    <span>© 2026 {escape(p['name'])} · {escape(p['role'])}</span>
    <span>{escape(p['location'])}</span>
  </footer>
</main>

<script>
(function(){{
  var btn=document.getElementById('copy'),note=document.getElementById('note'),addr=document.getElementById('addr');
  function pick(){{var r=document.createRange();r.selectNodeContents(addr);var s=window.getSelection();s.removeAllRanges();s.addRange(r);}}
  btn.addEventListener('click',function(){{
    var t=addr.textContent;
    var done=function(){{note.textContent='Email copied.';}};
    var fail=function(){{pick();note.textContent='Press Ctrl+C or Cmd+C to copy the selected address.';}};
    try{{navigator.clipboard.writeText(t).then(done,fail);}}catch(e){{fail();}}
  }});
}})();

/* Scroll motion fallback for browsers without CSS scroll-driven animations. */
(function(){{
  var native=window.CSS&&CSS.supports&&CSS.supports('animation-timeline: view()');
  var still=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(native||still)return;
  var root=document.documentElement;
  root.classList.add('js-anim');
  var sel='.sec-head,.card,.step,.why>div,.pstats>div,.contact>*,.stack,.case>div:first-child,.case .rows';
  var els=[].slice.call(document.querySelectorAll(sel));
  els.forEach(function(el){{
    el.classList.add('rv');
    if(el.matches('.case>div:first-child'))el.classList.add('rv-l');
    if(el.matches('.case .rows'))el.classList.add('rv-r');
  }});
  if('IntersectionObserver' in window){{
    var io=new IntersectionObserver(function(es){{
      es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});
    }},{{threshold:0.12,rootMargin:'0px 0px -6% 0px'}});
    els.forEach(function(el){{io.observe(el);}});
  }}else{{els.forEach(function(el){{el.classList.add('in');}});}}
  var hero=document.querySelector('.hero>div:first-child'),trace=document.querySelector('.trace'),bar=document.querySelector('.bar'),tick=false;
  function frame(){{
    tick=false;
    var y=window.pageYOffset||0,h=Math.max(1,window.innerHeight*0.85),t=Math.min(1,y/h);
    var max=Math.max(1,document.documentElement.scrollHeight-window.innerHeight);
    if(hero){{hero.style.transform='translateY('+(-90*t)+'px)';hero.style.opacity=String(1-0.85*t);}}
    if(trace)trace.style.transform='translateY('+(60*t)+'px)';
    bar.style.setProperty('--p',String(Math.min(1,y/max)));
  }}
  window.addEventListener('scroll',function(){{if(!tick){{tick=true;requestAnimationFrame(frame);}}}},{{passive:true}});
  frame();
}})();
</script>
</body>
</html>
"""
    out = Path(__file__).with_name("index.html")
    out.write_text(body, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")

if __name__ == "__main__":
    build()
