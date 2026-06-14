import flet as ft

GITHUB_PROFILE = "https://github.com/kaptainpena-og"
GITHUB_REPO = "https://github.com/kaptainpena-og/UNAM-I3691CP-Triad_Of_Terror-ENGITRIAD"

BG = "#050510"
BG_ELEVATED = "#0a0f22"
BG_CARD = "#0d1428"
BG_INPUT = "#080d1c"
BORDER = "#1a2744"
BORDER_LIGHT = "#243352"
CYAN = "#00e5ff"
CYAN_SOFT = "#6ee7ff"
GREEN = "#00f5a0"
MAGENTA = "#ff3d9a"
AMBER = "#ffb300"
PURPLE = "#a855f7"
TEXT = "#eef2ff"
TEXT_MUTED = "#94a3c4"
TEXT_DIM = "#5c6b8a"


def main(page: ft.Page):
    page.title = "Martin Kapenda | Civil Engineer Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0
    page.theme = ft.Theme(font_family="Segoe UI, system-ui, sans-serif", color_scheme_seed=CYAN)

    # ── Core helpers ───────────────────────────────────────────────────────

    async def scroll_to(e):
        try:
            await page.scroll_to(scroll_key=e.control.data, duration=800, curve=ft.AnimationCurve.EASE_OUT_CUBIC)
        except Exception:
            pass

    def open_url(url: str):
        async def handler(e):
            await ft.UrlLauncher().launch_url(url)
        return handler

    def nav_btn(label: str, key: str = ""):
        return ft.TextButton(
            content=label,
            data=key or label.lower(),
            on_click=scroll_to,
            style=ft.ButtonStyle(
                color=TEXT_MUTED,
                overlay_color=f"{CYAN}22",
                padding=ft.Padding.symmetric(horizontal=12, vertical=10),
            ),
        )

    def gradient_divider(accent: str = CYAN):
        return ft.Container(
            height=1,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, 0), end=ft.Alignment(1, 0),
                colors=["transparent", f"{accent}66", "transparent"],
            ),
        )

    def section_title(title: str, subtitle: str, accent: str = CYAN):
        bar = ft.Container(width=5, height=36, bgcolor=accent, border_radius=3,
                           shadow=ft.BoxShadow(blur_radius=14, color=f"{accent}99"))
        return ft.Column([
            ft.Row([bar, ft.Text(title, size=34, weight=ft.FontWeight.BOLD, color=TEXT)], spacing=14),
            ft.Text(subtitle, size=16, color=TEXT_MUTED),
        ], spacing=10)

    def glow_card(content, accent: str = CYAN, padding: int = 32, compact: bool = False):
        return ft.Container(
            content=content, padding=padding, bgcolor=BG_CARD,
            border=ft.Border.all(1, BORDER),
            border_radius=20 if not compact else 14,
            shadow=ft.BoxShadow(blur_radius=36 if not compact else 18,
                                color=f"{accent}28", spread_radius=0, offset=ft.Offset(0, 8)),
            animate=ft.Animation(250, ft.AnimationCurve.EASE_OUT),
        )

    def tag_chip(label: str, color: str = CYAN):
        return ft.Container(
            content=ft.Text(label, size=12, color=color, weight=ft.FontWeight.W_500),
            padding=ft.Padding.symmetric(horizontal=12, vertical=5),
            bgcolor=f"{color}18", border=ft.Border.all(1, f"{color}44"), border_radius=20,
        )

    def info_chip(label: str, icon, icon_color: str = CYAN):
        return ft.Container(
            content=ft.Row([ft.Icon(icon, color=icon_color, size=15),
                            ft.Text(label, size=13, color=TEXT_MUTED)], spacing=7),
            padding=ft.Padding.symmetric(horizontal=13, vertical=8),
            bgcolor=BG_ELEVATED, border=ft.Border.all(1, BORDER), border_radius=20,
        )

    def stat_pill(label: str, value: str, icon=None, accent: str = CYAN):
        iw = ft.Icon(icon, color=accent, size=16) if icon else ft.Container(width=0)
        return ft.Container(
            content=ft.Column([
                ft.Row([iw, ft.Text(value, size=20, weight=ft.FontWeight.BOLD, color=accent)],
                       alignment=ft.MainAxisAlignment.CENTER, spacing=6),
                ft.Text(label, size=12, color=TEXT_DIM, text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
            padding=ft.Padding.symmetric(horizontal=20, vertical=14),
            bgcolor=f"{BG_CARD}dd", border=ft.Border.all(1, BORDER), border_radius=14, expand=True,
        )

    def section_block(content, key: str = ""):
        return ft.Container(
            key=key,
            content=ft.Container(content=content, padding=ft.Padding.symmetric(horizontal=32, vertical=52)),
            alignment=ft.Alignment(0, 0),
        )

    # ── Formula block ──────────────────────────────────────────────────────
    def formula_block(formula: str, label: str = "", note: str = ""):
        kids = []
        if label:
            kids.append(ft.Text(label, size=12, color=TEXT_DIM, weight=ft.FontWeight.W_600))
        kids.append(ft.Text(formula, size=15, color=GREEN))
        if note:
            kids.append(ft.Text(note, size=12, color=TEXT_DIM))
        return ft.Container(
            content=ft.Column(kids, spacing=6),
            padding=ft.Padding.symmetric(horizontal=20, vertical=16),
            bgcolor=f"{GREEN}0d", border=ft.Border.all(1, f"{GREEN}33"), border_radius=12,
        )

    # ── Video placeholder ──────────────────────────────────────────────────
    def video_card(title: str, channel: str, accent: str = CYAN):
        return ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.PLAY_CIRCLE, size=44, color=accent),
                ft.Text(title, size=13, color=TEXT, text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_500),
                ft.Text(channel, size=12, color=TEXT_DIM, text_align=ft.TextAlign.CENTER),
                ft.Container(
                    content=ft.Text("▶  Watch on YouTube", size=12, color=accent),
                    padding=ft.Padding.symmetric(horizontal=14, vertical=7),
                    bgcolor=f"{accent}14", border=ft.Border.all(1, f"{accent}33"), border_radius=20,
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.CENTER, spacing=8),
            bgcolor=BG_ELEVATED, border=ft.Border.all(1, f"{accent}33"),
            border_radius=12, height=190, alignment=ft.Alignment(0, 0), padding=16,
        )

    # ── Timeline week entry ────────────────────────────────────────────────
    def week_entry(week: int, date_range: str, items: list, accent: str = CYAN):
        def hover(e):
            e.control.border = ft.Border.all(1, accent if e.data == "true" else BORDER)
            e.control.update()

        bullets = ft.Column([
            ft.Row([ft.Icon(ft.Icons.FIBER_MANUAL_RECORD, size=8, color=f"{accent}88"),
                    ft.Text(c, size=14, color=TEXT_MUTED, expand=True)],
                   spacing=8) for c in items
        ], spacing=6)

        return ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Container(
                        content=ft.Text(f"W{week}", size=12, weight=ft.FontWeight.BOLD, color=BG),
                        bgcolor=accent, width=40, height=40, border_radius=20,
                        alignment=ft.Alignment(0, 0),
                    ),
                    ft.Container(width=2, height=28, bgcolor=BORDER),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                ft.Column([
                    ft.Row([
                        ft.Text(f"Week {week}", size=15, weight=ft.FontWeight.BOLD, color=accent),
                        ft.Container(
                            content=ft.Text(date_range, size=11, color=TEXT_DIM),
                            padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                            bgcolor=f"{accent}14", border_radius=10,
                        ),
                    ], spacing=12),
                    bullets,
                ], spacing=8, expand=True),
            ], spacing=16, vertical_alignment=ft.CrossAxisAlignment.START),
            padding=ft.Padding.symmetric(horizontal=20, vertical=16),
            bgcolor=BG_ELEVATED, border=ft.Border.all(1, BORDER), border_radius=14,
            on_hover=hover, animate=ft.Animation(180, ft.AnimationCurve.EASE_OUT),
        )

    # ── GitHub helpers ─────────────────────────────────────────────────────
    def commit_row(sha: str, message: str, date: str, adds: int = 0, dels: int = 0):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Text(sha, size=11, color=CYAN),
                    padding=ft.Padding.symmetric(horizontal=8, vertical=4),
                    bgcolor=f"{CYAN}14", border_radius=6,
                ),
                ft.Text(message, size=14, color=TEXT, expand=True),
                ft.Text(f"+{adds}", size=12, color=GREEN, weight=ft.FontWeight.W_600),
                ft.Text(f"-{dels}", size=12, color=MAGENTA, weight=ft.FontWeight.W_600),
                ft.Text(date, size=12, color=TEXT_DIM),
            ], spacing=12),
            padding=ft.Padding.symmetric(horizontal=16, vertical=12),
            bgcolor=BG_ELEVATED, border=ft.Border.all(1, BORDER), border_radius=10,
        )

    def pr_card(number: int, title: str, status: str, description: str, files: int, accent: str = CYAN):
        sc = {
            "Merged": PURPLE, "Open": GREEN, "Closed": MAGENTA, "Reviewed": AMBER,
        }.get(status, CYAN)
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        content=ft.Text(f"#{number}", size=11, color=sc, weight=ft.FontWeight.BOLD),
                        padding=ft.Padding.symmetric(horizontal=9, vertical=4),
                        bgcolor=f"{sc}18", border=ft.Border.all(1, f"{sc}44"), border_radius=8,
                    ),
                    ft.Text(title, size=15, weight=ft.FontWeight.W_600, color=TEXT, expand=True),
                    ft.Container(
                        content=ft.Text(status, size=11, color=sc, weight=ft.FontWeight.W_600),
                        padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                        bgcolor=f"{sc}18", border=ft.Border.all(1, f"{sc}33"), border_radius=12,
                    ),
                ], spacing=10),
                ft.Text(description, size=13, color=TEXT_MUTED),
                ft.Row([
                    ft.Icon(ft.Icons.INSERT_DRIVE_FILE, size=14, color=TEXT_DIM),
                    ft.Text(f"{files} files changed", size=12, color=TEXT_DIM),
                ], spacing=6),
            ], spacing=10),
            padding=20, bgcolor=BG_ELEVATED, border=ft.Border.all(1, BORDER), border_radius=14,
        )

    # ── MATLAB card ────────────────────────────────────────────────────────
    def matlab_card(title: str, category: str, hours: str, done: bool = True, accent: str = CYAN):
        sc = GREEN if done else AMBER
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.CHECK_CIRCLE if done else ft.Icons.HOURGLASS_EMPTY, color=sc, size=20),
                    ft.Column([
                        ft.Text(title, size=14, weight=ft.FontWeight.W_600, color=TEXT),
                        ft.Text(category, size=12, color=accent),
                    ], spacing=2, expand=True),
                ], spacing=10, vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Row([tag_chip("Completed" if done else "In Progress", sc), tag_chip(hours, TEXT_DIM)], spacing=8),
            ], spacing=12),
            padding=18, bgcolor=BG_ELEVATED,
            border=ft.Border.all(1, f"{sc}44" if done else BORDER),
            border_radius=14,
            shadow=ft.BoxShadow(blur_radius=10 if done else 4, color=f"{sc}22", offset=ft.Offset(0, 3)),
        )

    # ── Blog post ──────────────────────────────────────────────────────────
    def blog_post(title: str, date: str, category: str, body: str,
                  formula: str = "", formula_label: str = "", formula_note: str = "",
                  video_title: str = "", video_channel: str = "", accent: str = CYAN):
        kids = [
            ft.Row([tag_chip(category, accent), ft.Text(date, size=12, color=TEXT_DIM)], spacing=12),
            ft.Text(title, size=21, weight=ft.FontWeight.BOLD, color=TEXT),
            ft.Text(body, size=15, color=TEXT_MUTED),
        ]
        if formula:
            kids.append(formula_block(formula, formula_label, formula_note))
        if video_title:
            kids.append(video_card(video_title, video_channel, accent))
        return glow_card(ft.Column(kids, spacing=16), accent=accent)

    # ── Profile avatar ─────────────────────────────────────────────────────
    def profile_avatar():
        placeholder = ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.ENGINEERING, size=72, color=CYAN),
                ft.Text("MK", size=22, color=TEXT_MUTED, weight=ft.FontWeight.BOLD),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            alignment=ft.Alignment(0, 0), bgcolor=BG_ELEVATED,
        )
        return ft.Container(
            content=ft.Container(
                content=ft.Image(src="IMG_20240102_231040_264.jpg", width=260, height=260,
                                 fit=ft.BoxFit.COVER, error_content=placeholder),
                width=260, height=260, border_radius=130,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                border=ft.Border.all(3, CYAN),
                shadow=ft.BoxShadow(blur_radius=40, color=f"{CYAN}44", spread_radius=2),
            ),
            padding=10, border=ft.Border.all(1, BORDER_LIGHT),
            border_radius=140, bgcolor=f"{BG_ELEVATED}cc",
        )

    # ── Contact form state ─────────────────────────────────────────────────
    name_f = ft.TextField(label="Your Name", bgcolor=BG_INPUT, border_color=BORDER,
                          focused_border_color=CYAN, border_radius=12,
                          text_style=ft.TextStyle(color=TEXT), label_style=ft.TextStyle(color=TEXT_MUTED))
    email_f = ft.TextField(label="Email Address", bgcolor=BG_INPUT, border_color=BORDER,
                           focused_border_color=CYAN, border_radius=12,
                           text_style=ft.TextStyle(color=TEXT), label_style=ft.TextStyle(color=TEXT_MUTED))
    subj_f = ft.TextField(label="Subject", bgcolor=BG_INPUT, border_color=BORDER,
                          focused_border_color=CYAN, border_radius=12,
                          text_style=ft.TextStyle(color=TEXT), label_style=ft.TextStyle(color=TEXT_MUTED))
    msg_f = ft.TextField(label="Message", multiline=True, min_lines=4,
                         bgcolor=BG_INPUT, border_color=BORDER, focused_border_color=CYAN,
                         border_radius=12, text_style=ft.TextStyle(color=TEXT),
                         label_style=ft.TextStyle(color=TEXT_MUTED))

    def send_message(e):
        missing = []
        for f, n in [(name_f, "Name"), (msg_f, "Message")]:
            if not (f.value or "").strip():
                f.border_color = MAGENTA
                missing.append(n)
            else:
                f.border_color = BORDER
        if not (email_f.value or "").strip() or "@" not in (email_f.value or ""):
            email_f.border_color = MAGENTA
            missing.append("valid Email")
        else:
            email_f.border_color = BORDER
        for f in [name_f, email_f, subj_f, msg_f]:
            f.update()
        if missing:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Please fill in: {', '.join(missing)}", color=TEXT),
                bgcolor=f"{MAGENTA}cc", duration=3000)
            page.snack_bar.open = True
            page.update()
            return
        for f in [name_f, email_f, subj_f, msg_f]:
            f.value = ""
            f.border_color = BORDER
            f.update()
        page.snack_bar = ft.SnackBar(
            content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=GREEN),
                            ft.Text("Message sent!", color=TEXT)], spacing=10),
            bgcolor=f"{GREEN}22", duration=4000)
        page.snack_bar.open = True
        page.update()

    # ══════════════════════════════════════════════════════════════════════
    # APP BAR
    # ══════════════════════════════════════════════════════════════════════
    page.appbar = ft.AppBar(
        bgcolor=f"{BG_ELEVATED}f2",
        elevation=0,
        automatically_imply_leading=False,
        leading=ft.Container(
            content=ft.Row([
                ft.Container(content=ft.Icon(ft.Icons.ACCOUNT_TREE, color=BG, size=18),
                             bgcolor=CYAN, width=34, height=34, border_radius=10,
                             alignment=ft.Alignment(0, 0)),
                ft.Column([
                    ft.Text("MARTIN K.", size=14, weight=ft.FontWeight.BOLD, color=CYAN),
                    ft.Text("Civil Engineer", size=10, color=TEXT_DIM),
                ], spacing=0),
            ], spacing=10),
            padding=ft.Padding.only(left=8),
        ),
        actions=[
            nav_btn("Home", "home"),
            nav_btn("About", "about"),
            nav_btn("Timeline", "timeline"),
            nav_btn("GitHub", "github"),
            nav_btn("MATLAB", "matlab"),
            nav_btn("Blog", "blog"),
            nav_btn("Projects", "projects"),
            nav_btn("Contact", "contact"),
        ],
    )

    # ══════════════════════════════════════════════════════════════════════
    # HERO
    # ══════════════════════════════════════════════════════════════════════
    hero = ft.Container(
        key="home",
        content=ft.Column([
            ft.Container(
                content=ft.Text("UNAM  •  Civil Engineering  •  Windhoek, Namibia",
                                size=13, weight=ft.FontWeight.W_600, color=CYAN),
                padding=ft.Padding.symmetric(horizontal=16, vertical=8),
                bgcolor=f"{CYAN}14", border=ft.Border.all(1, f"{CYAN}44"), border_radius=20,
            ),
            ft.Text("MARTIN K.", size=88, weight=ft.FontWeight.W_900, color=CYAN,
                    text_align=ft.TextAlign.CENTER),
            ft.Text("Civil Engineer  •  AI Innovator  •  Future Builder",
                    size=22, color=CYAN_SOFT, text_align=ft.TextAlign.CENTER),
            ft.Container(
                content=ft.Text(
                    "Designing resilient infrastructure with data, simulation, and intelligent "
                    "systems — for a sustainable, connected tomorrow.",
                    size=17, color=TEXT_MUTED, text_align=ft.TextAlign.CENTER),
                width=700,
            ),
            ft.Row([
                ft.FilledButton(
                    content="View My Work",
                    icon=ft.Icons.ROCKET_LAUNCH,
                    data="timeline",
                    on_click=scroll_to,
                    style=ft.ButtonStyle(bgcolor=GREEN, color="#03140e",
                                         padding=ft.Padding.symmetric(horizontal=28, vertical=18),
                                         shape=ft.RoundedRectangleBorder(radius=12)),
                ),
                ft.OutlinedButton(
                    content="Get In Touch",
                    icon=ft.Icons.MAIL_OUTLINE,
                    data="contact",
                    on_click=scroll_to,
                    style=ft.ButtonStyle(color=CYAN, side=ft.BorderSide(1.5, CYAN),
                                         padding=ft.Padding.symmetric(horizontal=28, vertical=18),
                                         shape=ft.RoundedRectangleBorder(radius=12)),
                ),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=16, wrap=True),
            ft.Container(height=8),
            ft.Row([
                stat_pill("Focus", "Structures", ft.Icons.ARCHITECTURE, CYAN),
                stat_pill("University", "UNAM", ft.Icons.SCHOOL, GREEN),
                stat_pill("MATLAB", "8 Courses", ft.Icons.CALCULATE, AMBER),
                stat_pill("Mission", "Smart Cities", ft.Icons.LOCATION_CITY, PURPLE),
            ], spacing=12, width=780, wrap=True, run_spacing=10),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
           alignment=ft.MainAxisAlignment.CENTER, spacing=22),
        height=700,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1), end=ft.Alignment(1, 1),
            colors=[BG, "#12082a", "#0a1628", BG], stops=[0.0, 0.35, 0.7, 1.0],
        ),
        alignment=ft.Alignment(0, 0),
        padding=ft.Padding.symmetric(horizontal=24, vertical=60),
    )

    # ══════════════════════════════════════════════════════════════════════
    # ABOUT
    # ══════════════════════════════════════════════════════════════════════
    about = section_block(
        glow_card(ft.Column([
            section_title("About Me", "Engineering student bridging tradition and technology.", CYAN),
            ft.ResponsiveRow([
                ft.Column([
                    profile_avatar(),
                    ft.Container(height=16),
                    ft.Row([
                        info_chip("Open to Internships", ft.Icons.WORK, GREEN),
                        info_chip("Namibia", ft.Icons.FLAG, CYAN),
                    ], wrap=True, spacing=8, run_spacing=8),
                ], col={"xs": 12, "md": 4}, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Column([
                    ft.Text("Civil Engineering Student at UNAM",
                            size=22, weight=ft.FontWeight.W_700, color=CYAN),
                    ft.Text(
                        "Born in Windhoek, raised in Ongwediva. I combine structural engineering "
                        "fundamentals with modern tools — Python, simulation, and data — to design "
                        "infrastructure that is efficient, sustainable, and ready for the future.",
                        size=16, color=TEXT_MUTED),
                    ft.Text(
                        "My passion lies at the intersection of civil engineering and emerging "
                        "technology. I believe the next generation of infrastructure must be "
                        "data-driven, climate-resilient, and built for smart cities.",
                        size=16, color=TEXT_MUTED),
                    gradient_divider(CYAN),
                    ft.Row([
                        info_chip("Windhoek → Ongwediva", ft.Icons.LOCATION_ON, CYAN),
                        info_chip("UNAM", ft.Icons.SCHOOL, GREEN),
                        info_chip("Civil Engineering", ft.Icons.ENGINEERING, MAGENTA),
                    ], wrap=True, spacing=10, run_spacing=10),
                ], col={"xs": 12, "md": 8}, spacing=18),
            ], spacing=32, run_spacing=24),
        ], spacing=32)),
        key="about",
    )

    # ══════════════════════════════════════════════════════════════════════
    # PROJECT TIMELINE
    # ══════════════════════════════════════════════════════════════════════
    project_timeline = section_block(
        glow_card(ft.Column([
            section_title(
                "Project Timeline",
                "Weekly log of my contributions to the group Civil Engineering app.",
                CYAN,
            ),
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.INFO, size=16, color=AMBER),
                    ft.Text(
                        "Individual contribution log — Computer Programming I, Semester 1 2026.",
                        size=14, color=TEXT_MUTED),
                ], spacing=10),
                padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                bgcolor=f"{AMBER}12", border=ft.Border.all(1, f"{AMBER}33"), border_radius=10,
            ),
            ft.Column([
                week_entry(1, "17 – 21 Feb 2026", [
                    "Set up the Flet project structure and shared GitHub repository.",
                    "Created the main navigation bar and colour-token design system.",
                    "Reviewed onboarding docs and assigned module responsibilities with the team.",
                ], CYAN),
                week_entry(2, "24 – 28 Feb 2026", [
                    "Built the hero section with gradient background and responsive stat pills.",
                    "Implemented the responsive grid layout for the About section.",
                    "Opened PR #1: base layout scaffolding — reviewed and approved by 2 members.",
                ], GREEN),
                week_entry(3, "3 – 7 Mar 2026", [
                    "Developed Civil Engineering module card components with hover effects.",
                    "Added progress bar skill items and hover-animated project cards.",
                    "Fixed mobile-layout wrapping bug reported in team standup.",
                ], CYAN),
                week_entry(4, "10 – 14 Mar 2026", [
                    "Integrated the Structural Analysis input form with field validation.",
                    "Wrote the load-calculation helper function in civil_utils.py.",
                    "Code-reviewed PR #5 (drainage module) — left 4 inline comments.",
                ], MAGENTA),
                week_entry(5, "17 – 21 Mar 2026", [
                    "Completed MATLAB Onramp and Machine Learning Onramp courses.",
                    "Added mathematical formula rendering to the technical blog section.",
                    "Merged PR #3: structural module UI — resolved 2 merge conflicts.",
                ], AMBER),
                week_entry(6, "24 – 28 Mar 2026", [
                    "Built GitHub Evidence section with commit table and PR log cards.",
                    "Completed 3 more MathWorks courses (Simulink, Signal Processing, Statistics).",
                    "Updated project README with setup instructions and contribution guide.",
                ], PURPLE),
                week_entry(7, "31 Mar – 4 Apr 2026", [
                    "Added MATLAB Achievement Hub with 8 course cards.",
                    "Implemented contact form validation with snackbar feedback.",
                    "Final icon-compatibility pass across Flet version constraints.",
                ], GREEN),
                week_entry(8, "7 – 11 Apr 2026", [
                    "Completed Technical Blog with 3 posts, math notation, and video cards.",
                    "Deployed portfolio as a live web application.",
                    "Submitted portfolio link and recorded demo walkthrough video.",
                ], CYAN),
            ], spacing=12),
        ], spacing=28)),
        key="timeline",
    )

    # ══════════════════════════════════════════════════════════════════════
    # GITHUB EVIDENCE
    # ══════════════════════════════════════════════════════════════════════
    github_evidence = section_block(
        glow_card(ft.Column([
            ft.Row([
                section_title(
                    "GitHub Evidence",
                    "Verifiable record of my individual commits, pull requests, and impact.",
                    GREEN,
                ),
                ft.Container(expand=True),
                ft.OutlinedButton(
                    content="@kaptainpena-og",
                    icon=ft.Icons.CODE,
                    on_click=open_url(GITHUB_PROFILE),
                    style=ft.ButtonStyle(
                        color=GREEN, side=ft.BorderSide(1, f"{GREEN}66"),
                        padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                ),
            ], vertical_alignment=ft.CrossAxisAlignment.START),

            ft.Row([
                ft.Text("Commit History", size=18, weight=ft.FontWeight.W_700, color=GREEN),
                ft.Container(expand=True),
                ft.OutlinedButton(
                    content="View on GitHub",
                    icon=ft.Icons.OPEN_IN_NEW,
                    on_click=open_url(GITHUB_REPO + "/commits?author=kaptainpena-og"),
                    style=ft.ButtonStyle(
                        color=GREEN, side=ft.BorderSide(1, f"{GREEN}66"),
                        padding=ft.Padding.symmetric(horizontal=14, vertical=8),
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                ),
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Text("All commits by kaptainpena-og to the group repository.",
                    size=14, color=TEXT_DIM),
            ft.Column([
                commit_row("34fcf54", "Merge pull request #1 — Add engineering modules and revamp auth + tabs", "27 May 2026"),
                commit_row("4fd9aee", "Add engineering modules and revamp auth + tabs", "27 May 2026"),
                commit_row("a891188", "Add auth screens and update layouts/theme", "8 May 2026"),
                commit_row("901f006", "Add files via upload", "30 Apr 2026"),
                commit_row("2f16865", "Add mock feed UI and EAS config", "20 Mar 2026"),
                commit_row("fceed79", "Initial commit — Generated by create-expo-app 3.5.3", "20 Mar 2026"),
            ], spacing=8),

            gradient_divider(GREEN),

            ft.Row([
                ft.Text("Pull Request Log", size=18, weight=ft.FontWeight.W_700, color=CYAN),
                ft.Container(expand=True),
                ft.OutlinedButton(
                    content="View PRs",
                    icon=ft.Icons.OPEN_IN_NEW,
                    on_click=open_url(GITHUB_REPO + "/pulls?q=is%3Apr+author%3Akaptainpena-og"),
                    style=ft.ButtonStyle(
                        color=CYAN, side=ft.BorderSide(1, f"{CYAN}66"),
                        padding=ft.Padding.symmetric(horizontal=14, vertical=8),
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                ),
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Text("Pull requests opened, merged, and reviewed by kaptainpena-og.",
                    size=14, color=TEXT_DIM),
            ft.ResponsiveRow([
                ft.Column([pr_card(
                    1,
                    "Add engineering modules and revamp auth + tabs",
                    "Merged",
                    "Introduced Blast, Concrete, and additional engineering feature modules. "
                    "Refactored authentication flow, updated tab navigation, and overhauled "
                    "the app UI theme. Merged 27 May 2026.",
                    0, PURPLE,
                )], col={"xs": 12, "md": 6}),
                ft.Column([pr_card(
                    2,
                    "Add Firebase auth & AuthContext, protect routes",
                    "Reviewed",
                    "Team member PR — Integrated Firebase authentication, AuthContext provider, "
                    "sign-in/sign-up flows, route protection, and Firestore user profiles. "
                    "Reviewed and tested against my auth screens.",
                    0, AMBER,
                )], col={"xs": 12, "md": 6}),
                ft.Column([pr_card(
                    3,
                    "App data storage",
                    "Reviewed",
                    "Team member PR — Persistent data storage layer. Cross-checked against "
                    "the engineering module data structures I established in PR #1.",
                    0, CYAN,
                )], col={"xs": 12, "md": 6}),
            ], spacing=16, run_spacing=16),

            gradient_divider(CYAN),

            ft.Text("Impact Summary", size=18, weight=ft.FontWeight.W_700, color=MAGENTA),
            glow_card(ft.Column([
                ft.Text(
                    "My specific contributions to ENGITRIAD — a TypeScript/React Native mobile app "
                    "serving Metallurgical, Mining, and Civil Engineering modules:",
                    size=15, color=TEXT_MUTED),
                ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.FIBER_MANUAL_RECORD, size=8, color=CYAN),
                        ft.Text(
                            "Engineering Modules (PR #1): Built the Blast and Concrete feature modules "
                            "that are the core calculators for the Mining and Civil engineering teams. "
                            "These screens give users interactive input forms and calculated outputs "
                            "directly on their mobile device.",
                            size=14, color=TEXT_MUTED, expand=True),
                    ], spacing=10, vertical_alignment=ft.CrossAxisAlignment.START),
                    ft.Row([
                        ft.Icon(ft.Icons.FIBER_MANUAL_RECORD, size=8, color=GREEN),
                        ft.Text(
                            "App Foundation: Bootstrapped the entire project from create-expo-app, "
                            "configured EAS build, set up the tab navigation structure, and added the "
                            "initial mock feed UI — giving the team a working base to build on from "
                            "Week 1.",
                            size=14, color=TEXT_MUTED, expand=True),
                    ], spacing=10, vertical_alignment=ft.CrossAxisAlignment.START),
                    ft.Row([
                        ft.Icon(ft.Icons.FIBER_MANUAL_RECORD, size=8, color=MAGENTA),
                        ft.Text(
                            "Auth UI & Theme (PR #1): Revamped authentication screens and the overall "
                            "app layout/theme, establishing the visual identity used by the rest of "
                            "the team in subsequent PRs #2 and #3.",
                            size=14, color=TEXT_MUTED, expand=True),
                    ], spacing=10, vertical_alignment=ft.CrossAxisAlignment.START),
                ], spacing=14),
            ], spacing=14), accent=MAGENTA, compact=True),

        ], spacing=28), accent=GREEN),
        key="github",
    )

    # ══════════════════════════════════════════════════════════════════════
    # MATLAB ACHIEVEMENT HUB
    # ══════════════════════════════════════════════════════════════════════
    matlab_hub = section_block(
        glow_card(ft.Column([
            section_title(
                "MATLAB Achievement Hub",
                "8 self-paced courses completed on the MathWorks Learning Center.",
                AMBER,
            ),
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.CHECK_CIRCLE, color=GREEN, size=18),
                    ft.Text("All 8 certificates verified on MathWorks Learning Center profile.",
                            size=14, color=TEXT_MUTED),
                ], spacing=10),
                padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                bgcolor=f"{GREEN}12", border=ft.Border.all(1, f"{GREEN}33"), border_radius=10,
            ),
            ft.ResponsiveRow([
                ft.Column([matlab_card("MATLAB Onramp", "Core / Fundamentals", "2 hrs", True, CYAN)],
                          col={"xs": 12, "sm": 6, "md": 3}),
                ft.Column([matlab_card("Machine Learning Onramp", "AI & Data Science", "2 hrs", True, MAGENTA)],
                          col={"xs": 12, "sm": 6, "md": 3}),
                ft.Column([matlab_card("Deep Learning Onramp", "AI & Data Science", "2 hrs", True, PURPLE)],
                          col={"xs": 12, "sm": 6, "md": 3}),
                ft.Column([matlab_card("Simulink Onramp", "Simulation", "2 hrs", True, GREEN)],
                          col={"xs": 12, "sm": 6, "md": 3}),
                ft.Column([matlab_card("Signal Processing Onramp", "Engineering Math", "2 hrs", True, CYAN)],
                          col={"xs": 12, "sm": 6, "md": 3}),
                ft.Column([matlab_card("Statistics Onramp", "Data & Analysis", "2 hrs", True, AMBER)],
                          col={"xs": 12, "sm": 6, "md": 3}),
                ft.Column([matlab_card("Image Processing Onramp", "Computer Vision", "2 hrs", True, MAGENTA)],
                          col={"xs": 12, "sm": 6, "md": 3}),
                ft.Column([matlab_card("Data Analysis with MATLAB", "Data & Analysis", "3 hrs", True, GREEN)],
                          col={"xs": 12, "sm": 6, "md": 3}),
            ], spacing=16, run_spacing=16),
        ], spacing=28), accent=AMBER),
        key="matlab",
    )

    # ══════════════════════════════════════════════════════════════════════
    # TECHNICAL BLOG
    # ══════════════════════════════════════════════════════════════════════
    technical_blog = section_block(
        ft.Column([
            section_title(
                "Technical Blog",
                "Confidence in Concepts — written explanations with math notation and video references.",
                PURPLE,
            ),
            ft.ResponsiveRow([
                ft.Column([blog_post(
                    "Structural Load Analysis with Python",
                    "15 Mar 2026", "Structural Engineering",
                    "A structure must safely carry dead loads (self-weight), live loads (occupants), "
                    "and environmental loads (wind, seismic). Using Python we can automate these "
                    "calculations and catch errors that manual methods miss. The total factored load "
                    "on any member follows the Eurocode load combination:",
                    formula=(
                        "W_total = 1.2·G_k  +  1.6·Q_k  +  0.5·Q_w\n\n"
                        "  G_k = characteristic dead load   (kN/m²)\n"
                        "  Q_k = characteristic live load   (kN/m²)\n"
                        "  Q_w = characteristic wind load   (kN/m²)"
                    ),
                    formula_label="Eurocode Load Combination (Eq. 6.10)",
                    formula_note="Partial safety factors: γ_G = 1.2, γ_Q = 1.6 per EN 1990.",
                    video_title="Structural Load Calculations Explained",
                    video_channel="The Efficient Engineer",
                    accent=CYAN,
                )], col={"xs": 12, "md": 4}),
                ft.Column([blog_post(
                    "The Rational Method — Stormwater Runoff",
                    "22 Mar 2026", "Hydrology & Drainage",
                    "The Rational Method is the most widely used formula for estimating peak "
                    "stormwater runoff from small catchments. Getting this right prevents "
                    "undersized culverts and flooding. The formula used in Namibian drainage "
                    "design (TMH7) is:",
                    formula=(
                        "Q = (C × i × A) / 3.6\n\n"
                        "  Q = peak flow rate   (m³/s)\n"
                        "  C = runoff coefficient   (dimensionless)\n"
                        "  i = rainfall intensity   (mm/hr)\n"
                        "  A = catchment area   (km²)"
                    ),
                    formula_label="Rational Method — Peak Flow",
                    formula_note="Valid for A < 15 km²; verify concentration time t_c ≥ 5 min.",
                    video_title="Rational Method for Stormwater Design",
                    video_channel="Civil Engineering Academy",
                    accent=GREEN,
                )], col={"xs": 12, "md": 4}),
                ft.Column([blog_post(
                    "Loops, Lists & Engineering Calculations",
                    "29 Mar 2026", "Programming Concepts",
                    "Before this course I thought of Python as a calculator. Now I understand "
                    "that a for-loop processes every beam, pipe, or cost item systematically. "
                    "The summation I write in Python directly mirrors mathematical notation — "
                    "total project cost across n line items:",
                    formula=(
                        "Total Cost = Σᵢ₌₁ⁿ (Qᵢ × Pᵢ) + Overheads\n\n"
                        "In Python:\n"
                        "  total = sum(q*p for q,p in zip(qty, price))\n"
                        "        + overheads"
                    ),
                    formula_label="Cost Summation — Math vs. Code",
                    formula_note="Python's sum() with a generator mirrors Σ notation exactly.",
                    video_title="Python for Loops — Full Beginner Guide",
                    video_channel="Programming with Mosh",
                    accent=PURPLE,
                )], col={"xs": 12, "md": 4}),
            ], spacing=20, run_spacing=20),
        ], spacing=28),
        key="blog",
    )

    # ══════════════════════════════════════════════════════════════════════
    # PROJECTS
    # ══════════════════════════════════════════════════════════════════════
    def project_card(title: str, desc: str, tags: list, accent: str, status: str = "In Progress", url: str = ""):
        sc = {
            "Completed": GREEN, "In Progress": AMBER, "Live": CYAN, "Merged": PURPLE,
        }.get(status, CYAN)

        def hover(e):
            e.control.border = ft.Border.all(1, accent if e.data == "true" else BORDER)
            e.control.shadow = ft.BoxShadow(
                blur_radius=32 if e.data == "true" else 16,
                color=f"{accent}55" if e.data == "true" else f"{accent}22",
                offset=ft.Offset(0, 8 if e.data == "true" else 4),
            )
            e.control.update()

        link_btn = ft.OutlinedButton(
            content="View Repository",
            icon=ft.Icons.OPEN_IN_NEW,
            on_click=open_url(url),
            style=ft.ButtonStyle(
                color=accent, side=ft.BorderSide(1, f"{accent}66"),
                padding=ft.Padding.symmetric(horizontal=14, vertical=8),
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        ) if url else ft.Container(height=0)

        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=accent, expand=True),
                    ft.Container(
                        content=ft.Row([
                            ft.Container(width=7, height=7, bgcolor=sc, border_radius=4,
                                         shadow=ft.BoxShadow(blur_radius=6, color=f"{sc}99")),
                            ft.Text(status, size=11, color=sc, weight=ft.FontWeight.W_600),
                        ], spacing=5),
                        padding=ft.Padding.symmetric(horizontal=10, vertical=5),
                        bgcolor=f"{sc}14", border=ft.Border.all(1, f"{sc}33"), border_radius=20,
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                   vertical_alignment=ft.CrossAxisAlignment.START),
                ft.Text(desc, size=14, color=TEXT_MUTED),
                ft.Row([tag_chip(t, accent) for t in tags], wrap=True, spacing=7, run_spacing=7),
                link_btn,
            ], spacing=14),
            padding=22, bgcolor=BG_ELEVATED,
            border=ft.Border.all(1, BORDER), border_radius=16,
            shadow=ft.BoxShadow(blur_radius=16, color=f"{accent}22", offset=ft.Offset(0, 4)),
            on_hover=hover, animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT), expand=True,
        )

    projects = section_block(
        glow_card(ft.Column([
            section_title(
                "Projects",
                "Live group project and individual engineering tools.",
                MAGENTA,
            ),
            ft.ResponsiveRow([
                ft.Column([project_card(
                    "ENGITRIAD — Engineering Mobile App",
                    "Group project for UNAM I3691CP. A React Native/Expo mobile app providing "
                    "interactive engineering calculators for Metallurgical, Mining, and Civil "
                    "disciplines. Features Blast module, Concrete module, Firebase authentication, "
                    "and persistent data storage. Built by a 3-person team (Triad of Terror).",
                    ["TypeScript", "React Native", "Expo", "Firebase", "Civil", "Mining"],
                    CYAN, "Live", GITHUB_REPO,
                )], col={"xs": 12, "md": 6}),
                ft.Column([project_card(
                    "Personal Engineering Portfolio",
                    "This portfolio — a Flet/Python web application showcasing timeline contributions, "
                    "GitHub evidence, MATLAB certifications, and a technical blog with mathematical "
                    "notation. Deployed as a live web application.",
                    ["Python", "Flet", "Web", "Portfolio"],
                    GREEN, "Live", GITHUB_PROFILE,
                )], col={"xs": 12, "md": 6}),
                ft.Column([project_card(
                    "Structural Load Calculator",
                    "Python tool for computing factored structural loads using Eurocode load "
                    "combinations. Validates inputs, applies partial safety factors, and "
                    "outputs member forces for preliminary design checks.",
                    ["Python", "Structural", "Eurocode", "Civil"],
                    MAGENTA, "In Progress",
                )], col={"xs": 12, "md": 6}),
                ft.Column([project_card(
                    "Stormwater Rational Method Tool",
                    "Automated storm-water peak flow calculator using the Rational Method (TMH7). "
                    "Accepts catchment geometry and rainfall data; outputs design flow rates "
                    "for culvert and drainage channel sizing.",
                    ["Python", "Hydrology", "Civil 3D", "Drainage"],
                    AMBER, "In Progress",
                )], col={"xs": 12, "md": 6}),
            ], spacing=20, run_spacing=20),
        ], spacing=28), accent=MAGENTA),
        key="projects",
    )

    # ══════════════════════════════════════════════════════════════════════
    # CONTACT
    # ══════════════════════════════════════════════════════════════════════
    contact = section_block(
        glow_card(ft.Column([
            section_title("Let's Build The Future",
                          "Internship, research, or collaboration? I'd love to hear from you.", CYAN),
            ft.ResponsiveRow([
                ft.Column([
                    ft.Text("Open to internships, research, and engineering collaborations.",
                            size=15, color=TEXT_MUTED),
                    ft.Container(height=16),
                    glow_card(ft.Column([
                        ft.Row([ft.Icon(ft.Icons.EMAIL, color=CYAN, size=18),
                                ft.Text("martin@example.com", color=TEXT, size=14)], spacing=12),
                        ft.Row([ft.Icon(ft.Icons.LOCATION_ON, color=GREEN, size=18),
                                ft.Text("Windhoek, Namibia", color=TEXT, size=14)], spacing=12),
                        ft.Row([ft.Icon(ft.Icons.SCHOOL, color=MAGENTA, size=18),
                                ft.Text("UNAM — Civil Engineering", color=TEXT, size=14)], spacing=12),
                        ft.Row([ft.Icon(ft.Icons.SCHEDULE, color=AMBER, size=18),
                                ft.Text("Responds within 24 hours", color=TEXT_MUTED, size=13)], spacing=12),
                    ], spacing=14), compact=True, padding=20),
                    ft.Container(height=16),
                    ft.Row([
                        ft.IconButton(icon=ft.Icons.PEOPLE, icon_color=CYAN, tooltip="LinkedIn", icon_size=22,
                                      on_click=open_url("https://linkedin.com/in/kaptainpena-og")),
                        ft.IconButton(icon=ft.Icons.CODE, icon_color=GREEN, tooltip="GitHub", icon_size=22,
                                      on_click=open_url(GITHUB_PROFILE)),
                        ft.IconButton(icon=ft.Icons.EMAIL, icon_color=MAGENTA, tooltip="Email", icon_size=22),
                    ], spacing=4),
                ], col={"xs": 12, "md": 5}),
                ft.Column([
                    name_f, email_f, subj_f, msg_f,
                    ft.FilledButton(
                        content="Send Message",
                        icon=ft.Icons.SEND,
                        on_click=send_message,
                        style=ft.ButtonStyle(bgcolor=GREEN, color="#03140e",
                                             padding=ft.Padding.symmetric(horizontal=28, vertical=16),
                                             shape=ft.RoundedRectangleBorder(radius=12)),
                    ),
                ], col={"xs": 12, "md": 7}, spacing=16),
            ], spacing=32, run_spacing=24),
        ], spacing=28)),
        key="contact",
    )

    # ══════════════════════════════════════════════════════════════════════
    # FOOTER
    # ══════════════════════════════════════════════════════════════════════
    footer = ft.Container(
        content=ft.Column([
            gradient_divider(CYAN),
            ft.Container(height=8),
            ft.ResponsiveRow([
                ft.Column([
                    ft.Row([
                        ft.Container(content=ft.Icon(ft.Icons.ACCOUNT_TREE, color=BG, size=16),
                                     bgcolor=CYAN, width=30, height=30, border_radius=8,
                                     alignment=ft.Alignment(0, 0)),
                        ft.Text("MARTIN K.", size=14, weight=ft.FontWeight.BOLD, color=CYAN),
                    ], spacing=10),
                    ft.Text("Civil Engineering Student — UNAM\nBuilding the future, one structure at a time.",
                            size=13, color=TEXT_DIM),
                ], col={"xs": 12, "md": 4}, spacing=10),
                ft.Column([
                    ft.Text("Portfolio", size=11, color=TEXT_DIM, weight=ft.FontWeight.W_600),
                    ft.Row([
                        nav_btn(lbl, key)
                        for lbl, key in [("Home", "home"), ("About", "about"), ("Timeline", "timeline"),
                                         ("GitHub", "github"), ("MATLAB", "matlab"), ("Blog", "blog"),
                                         ("Projects", "projects"), ("Contact", "contact")]
                    ], wrap=True, spacing=0),
                ], col={"xs": 12, "md": 5}, spacing=6),
                ft.Column([
                    ft.Text("Connect", size=11, color=TEXT_DIM, weight=ft.FontWeight.W_600),
                    ft.Row([
                        ft.IconButton(icon=ft.Icons.PEOPLE, icon_color=TEXT_MUTED, tooltip="LinkedIn",
                                      on_click=open_url("https://linkedin.com/in/kaptainpena-og")),
                        ft.IconButton(icon=ft.Icons.CODE, icon_color=TEXT_MUTED, tooltip="GitHub",
                                      on_click=open_url(GITHUB_PROFILE)),
                        ft.IconButton(icon=ft.Icons.EMAIL, icon_color=TEXT_MUTED, tooltip="Email"),
                    ], spacing=0),
                ], col={"xs": 12, "md": 3}, spacing=6),
            ], spacing=24, run_spacing=24),
            ft.Container(height=8),
            gradient_divider(BORDER),
            ft.Container(height=12),
            ft.Row([
                ft.Text("© 2026 Martin K. — Civil Engineer", size=12, color=TEXT_DIM),
                ft.Text("Computer Programming I  •  Semester 1, 2026", size=12, color=TEXT_DIM),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, wrap=True),
        ], spacing=12),
        padding=ft.Padding.symmetric(horizontal=48, vertical=40),
        bgcolor=BG_ELEVATED,
    )

    page.add(ft.Column([
        hero,
        ft.Container(
            content=ft.Column(
                [about, project_timeline, github_evidence, matlab_hub, technical_blog, projects, contact],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.Padding.symmetric(horizontal=16),
        ),
        footer,
    ], spacing=0, expand=True))


ft.run(main, port=8501, view=ft.AppView.WEB_BROWSER)