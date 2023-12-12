import os

def replace_text_in_files(folder_path, replace_list):
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

            for old_text, new_text in replace_list:
                file_content = file_content.replace(old_text, new_text)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(file_content)

            print(f'Replaced text in {filename}')

if __name__ == "__main__":
    folder_path = '.'
    replace_list = [
        ('Jean Camargo', 'John Wick'),
        ('Eduardo Bellis', 'Sofia Reis'),
        #('dashboard/pulse', 'obi_dashboard_pulse.html'),
        ('Admin Ob', 'Web app'),
        ('Mercadolibre', 'My Company'),
        ('http://localhost:3000/dashboard/metrics/sprints_board_view', 'obi_dashboard_metrics_sprints_board_view.html'),
        ('http://localhost:3000/dashboard/metrics/code', 'obi_dashboard_metrics_code.html'),
        ('http://localhost:3000/dashboard/metrics/methodology', 'obi_dashboard_metrics_methodology.html'),
        ('http://localhost:3000/dashboard/metrics', 'obi_dashboard_metrics_overview.html'),
        ('http://localhost:3000/dashboard/pulse', 'obi_dashboard_pulse.html'),
        ('http://localhost:3000/actions/all', 'obi_actions_all_actions.html'),
        ('http://localhost:3000/actions/your_actions', 'obi_actions_your_actions.html'),
        ('http://localhost:3000/actions/scheduled_actions', 'obi_actions_scheduled_actions.html'),
        ('http://localhost:3000/actions/manual_actions', 'obi_actions_manual_actions.html'),
        ('http://localhost:3000/services/connections', 'obi_services_connections.html'),
        ('http://localhost:3000/squad_logs', 'obi_team_logs.html'),
        ('http://localhost:3000/alerts/all', 'obi_alerts_all_alerts.html'),
        ('http://localhost:3000/alerts/your_alerts', 'obi_alerts_your_alerts.html'),
        ('http://localhost:3000/alerts/squads_alerts', 'obi_alerts_teams_alerts_admin.html'),
        ('id="your_alerts" href="obi_alerts_teams_alerts_admin.html"', 'id="your_alerts" href="obi_alerts_your_alerts.html"'),
        ('Highlight - comportamiento destacado', 'Highlight - Outstanding Behavior'),
        ('Front end', 'Frontend'),
        ('Mercado Libre', 'My Company'),
        ('My Company#9', 'My Company'),
        ('My Company#13', 'My Company'),
        ('My Company#5', 'My Company'),
        ('#298 - Compromisos', 'Compromises'),
        ('#133 - Feedback Planning Meeting', 'Feedback Planning Meeting'),
        ('#364 - Cierre de Sprint', 'Sprint Closing'),
        ('#136 - Retro Meeting', 'Retro Meeting'),
        ('Iniciativa', 'Initiative'),
        ('Inteligencia social/ relacional', 'Social/Relational Intelligence'),
        ('Influencia', 'Influence'),
        ('Autonomía', 'Autonomy'),
        ('Desarrollo de Personas', 'Development of People'),
        ('Orientación al servicio', 'Service-oriented'),
        ('Precisión', 'Precision'),
        ('Atención focalizada', 'Focused attention'),
        ('Pensamiento analítico', 'Analytical thinking'),
        ('Excelencia Técnica', 'Tecnical excellence'),
        ('Implementación', 'Implementation'),
        ('Expeditividad', 'Promptness'),
        ('Diplomacia', 'Diplomacy'),
        ('Disponibilidad', 'Availability'),
        ('Agente de cambio', 'Change agent'),
        ('Determinación', 'Determination'),
        ('Receptivo', 'Receptive'),
        ('#133 - Zaira Villegas', 'Zaira Villegas'),
        ('Andre Lucas', 'Evelyn Doria'),
        ('Abner Batista', 'Edgar Cruz'),
        ('Alexia Andrade Calmon Diaz', 'Sofia Mesa'),
        ('Roberto Ferraz', 'Leo Donnel'),
        ('<link rel="apple-touch-icon" href="http://localhost:3000/logo192.png">', ''),
        ('<link rel="manifest" href="http://localhost:3000/manifest.json">', ''),
        ('<link rel="icon" href="http://localhost:3000/favicon.ico">', ''),
        ('<head>', "<head><link href='favicon.ico' rel='icon' />"),
        ('Gigi se muestra muy receptiva al feedbac...', 'Sofia is very receptive to feedback...'),
        ('Durante las primeras semanas de entrenam...', 'During the first weeks of training...'),
        ('Santi estuvo trabajando en conjunto con ...', 'Leo was working together with his colleagues..'),
        ('A Santi le cuesta muchísimo exponer en d...', 'Leo finds it very difficult to present...'),
        ('En las primeras interacciones con el equ...', 'In the first interactions with the team...'),
        ('Repo: melisource/fury_mp-admin-home', 'Repo: frontend/apiservices'),
        ('Repo: melisource/fury_mp-admin-onboarding-backend', 'Repo: frontend/apiservices'),
        ('Calendar: mayaly.villalobos@teamcubation.com', 'Calendar: zaira.vi@teamcubation.com'),
        ('Project: Admin Onboarding  (mercadolibre space) - Board: Admin Onboarding Scrum', 'Project: webapi'),
        ('Repo: osalomon89/meli-items-w2', 'Repo: frontend/apiservices'),
        ('<button class="MuiButtonBase-root css-10rlfvr-MuiButtonBase-root"', '<button id="nav-button-toogle" class="MuiButtonBase-root css-10rlfvr-MuiButtonBase-root"'),
        ('nav class="MuiBox-root css-rs0zx6"', 'nav id="nav-container" class="MuiBox-root css-rs0zx6"'),
        ('<div class="react-draggable MuiBox-root css-1089dj4" style="transform: translate(-31px, -31px);"><div class="MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-pwcg7p-MuiCollapse-root" style="min-height: 0px;"><div class="MuiCollapse-wrapper MuiCollapse-vertical css-smkl36-MuiCollapse-wrapper"><div class="MuiCollapse-wrapperInner MuiCollapse-vertical css-9l5vo-MuiCollapse-wrapperInner"><div class="MuiBox-root css-0" style="display: grid; padding-top: 1px; padding-bottom: 1px;"><div><button class="MuiButtonBase-root MuiFab-root MuiFab-extended MuiFab-sizeSmall MuiFab-primary css-o7387c-MuiButtonBase-root-MuiFab-root" tabindex="0" type="button">Team Log<svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-2zunby-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="AddIcon"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></svg><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></button></div></div></div></div></div><button class="MuiButtonBase-root MuiFab-root MuiFab-circular MuiFab-sizeLarge MuiFab-primary css-1vuye2k-MuiButtonBase-root-MuiFab-root" tabindex="0" type="button" id="floating-actions-menu" aria-label="add"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-i4bv87-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="MenuIcon"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></button></div>', ''),
        ('<div class="react-draggable MuiBox-root css-1089dj4" style="transform: translate(-1149px, 36px);"><div class="MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-pwcg7p-MuiCollapse-root" style="min-height: 0px;"><div class="MuiCollapse-wrapper MuiCollapse-vertical css-smkl36-MuiCollapse-wrapper"><div class="MuiCollapse-wrapperInner MuiCollapse-vertical css-9l5vo-MuiCollapse-wrapperInner"><div class="MuiBox-root css-0" style="display: grid; padding-top: 1px; padding-bottom: 1px;"><div><button class="MuiButtonBase-root MuiFab-root MuiFab-extended MuiFab-sizeSmall MuiFab-primary css-o7387c-MuiButtonBase-root-MuiFab-root" tabindex="0" type="button">Team Log<svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-2zunby-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="AddIcon"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"></path></svg><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></button></div></div></div></div></div><button class="MuiButtonBase-root MuiFab-root MuiFab-circular MuiFab-sizeLarge MuiFab-primary css-1vuye2k-MuiButtonBase-root-MuiFab-root" tabindex="0" type="button" id="floating-actions-menu" aria-label="add"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-i4bv87-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="MenuIcon"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></button></div>', ''),
        ('height: 100%; }/* Slider */.slick-slider', 'height: 100%; overflow-y:scroll !important; }/* Slider */.slick-slider'),
        ('<li>#2841 - Team: Frontend - Service: GitHub</li><li>#2840 - Team: Frontend - Service: GitHub</li><li>#1817 - Team: Frontend - Service: Google Calendar</li>', ''),
        ('<span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a></div></div></div></div><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-buwwzh-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="squad-logs" href="obi_team_logs.html" target="_self"><div class="MuiListItemIcon-root css-1jsj0xp-MuiListItemIcon-root"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-list-check" width="1.3rem" height="1.3rem" viewBox="0 0 24 24" stroke-width="1.5" stroke="#F34E1E" fill="none" stroke-linecap="round" stroke-linejoin="round"><desc>Download more icon variants from https://tabler-icons.io/i/list-check</desc><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M3.5 5.5l1.5 1.5l2.5 -2.5"></path><path d="M3.5 11.5l1.5 1.5l2.5 -2.5"></path><path d="M3.5 17.5l1.5 1.5l2.5 -2.5"></path><line x1="11" y1="6" x2="20" y2="6"></line><line x1="11" y1="12" x2="20" y2="12"></line><line x1="11" y1="18" x2="20" y2="18"></line></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Team logs</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><div class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-buwwzh-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button"><div class="MuiListItemIcon-root css-1jsj0xp-MuiListItemIcon-root"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-users" width="1.3rem" height="1.3rem" viewBox="0 0 24 24" stroke-width="1.5" stroke="#F34E1E" fill="none" stroke-linecap="round" stroke-linejoin="round" style="margin-top: auto; margin-bottom: auto;"><desc>Download more icon variants from https://tabler-icons.io/i/users</desc><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><circle cx="9" cy="7" r="4"></circle><path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path><path d="M21 21v-2a4 4 0 0 0 -3 -3.85"></path></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-llyvih-MuiTypography-root">Administration</p></div><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-chevron-up" width="1rem" height="1rem" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="margin-top: auto; margin-bottom: auto;"><desc>Download more icon variants from https://tabler-icons.io/i/chevron-up</desc><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><polyline points="6 15 12 9 18 15"></polyline></svg><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></div><div class="MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-pwcg7p-MuiCollapse-root" style="min-height: 0px;"><div class="MuiCollapse-wrapper MuiCollapse-vertical css-smkl36-MuiCollapse-wrapper"><div class="MuiCollapse-wrapperInner MuiCollapse-vertical css-9l5vo-MuiCollapse-wrapperInner"><div class="MuiList-root css-1e3abne-MuiList-root"><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="credits" href="http://localhost:3000/credit_usages" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Credits</p></div><div class="MuiChip-root MuiChip-filled MuiChip-sizeSmall MuiChip-colorSecondary MuiChip-filledSecondary css-16vv9uc-MuiChip-root"><span class="MuiChip-label MuiChip-labelSmall css-t3ycia-MuiChip-label">17</span></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="users" href="http://localhost:3000/admin/users" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Users</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="clients" href="http://localhost:3000/admin/clients" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Clients</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="squads" href="http://localhost:3000/admin/squads" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Teams</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="actions_admin" href="http://localhost:3000/admin/actions_admin" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Actions admin</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="training_plans" href="http://localhost:3000/admin/training_plans" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Training Plans</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="squad_log_types" href="http://localhost:3000/admin/squad_log_types" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Team Log Types</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="tags" href="http://localhost:3000/admin/tags" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Tags</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="generate_report" href="http://localhost:3000/admin/generate_report" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Generate Report</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a></div></div></div></div>', ''),
        ('<span class="MuiSwitch-root MuiSwitch-sizeMedium css-o94zi1-MuiSwitch-root"><span class="MuiSwitch-switchBase MuiSwitch-colorPrimary MuiButtonBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary PrivateSwitchBase-root css-15b8ibt-MuiButtonBase-root-MuiSwitch-switchBase"><input class="MuiSwitch-input PrivateSwitchBase-input css-1m9pwf3" type="checkbox"><span class="MuiSwitch-thumb css-jsexje-MuiSwitch-thumb"></span><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></span><span class="MuiSwitch-track css-1pbwew3-MuiSwitch-track"></span></span>', ''),
        ('<a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="actions_metrics" href="http://localhost:3000/dashboard/actions_metrics" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Actions Metrics</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a>', ''),
        ('<a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="skills_snapshots" href="http://localhost:3000/dashboard/skills_snapshots" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Skills Snapshots</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a>', ''),
        ('<a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="collected_data" href="http://localhost:3000/services/collected_data" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Collected data</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a>', ''),
        ('<a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="metric_data" href="http://localhost:3000/services/metric_data" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Metric data</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a>', ''),
        ('<a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="compliance" href="http://localhost:3000/actions/compliance" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Compliance</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a>', ''),
        ('<a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-buwwzh-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="education" href="http://localhost:3000/education" target="_self"><div class="MuiListItemIcon-root css-1jsj0xp-MuiListItemIcon-root"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-book" width="1.3rem" height="1.3rem" viewBox="0 0 24 24" stroke-width="1.5" stroke="#F34E1E" fill="none" stroke-linecap="round" stroke-linejoin="round"><desc>Download more icon variants from https://tabler-icons.io/i/book</desc><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M3 19a9 9 0 0 1 9 0a9 9 0 0 1 9 0"></path><path d="M3 6a9 9 0 0 1 9 0a9 9 0 0 1 9 0"></path><line x1="3" y1="6" x2="3" y2="19"></line><line x1="12" y1="6" x2="12" y2="19"></line><line x1="21" y1="6" x2="21" y2="19"></line></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Education</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a>', ''),
        ('<div class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-buwwzh-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button"><div class="MuiListItemIcon-root css-1jsj0xp-MuiListItemIcon-root"><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-users" width="1.3rem" height="1.3rem" viewBox="0 0 24 24" stroke-width="1.5" stroke="#F34E1E" fill="none" stroke-linecap="round" stroke-linejoin="round" style="margin-top: auto; margin-bottom: auto;"><desc>Download more icon variants from https://tabler-icons.io/i/users</desc><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><circle cx="9" cy="7" r="4"></circle><path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path><path d="M21 21v-2a4 4 0 0 0 -3 -3.85"></path></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-llyvih-MuiTypography-root">Administration</p></div><svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-chevron-up" width="1rem" height="1rem" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="margin-top: auto; margin-bottom: auto;"><desc>Download more icon variants from https://tabler-icons.io/i/chevron-up</desc><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><polyline points="6 15 12 9 18 15"></polyline></svg><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></div><div class="MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-pwcg7p-MuiCollapse-root" style="min-height: 0px;"><div class="MuiCollapse-wrapper MuiCollapse-vertical css-smkl36-MuiCollapse-wrapper"><div class="MuiCollapse-wrapperInner MuiCollapse-vertical css-9l5vo-MuiCollapse-wrapperInner"><div class="MuiList-root css-1e3abne-MuiList-root"><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="credits" href="http://localhost:3000/credit_usages" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Credits</p></div><div class="MuiChip-root MuiChip-filled MuiChip-sizeSmall MuiChip-colorSecondary MuiChip-filledSecondary css-16vv9uc-MuiChip-root"><span class="MuiChip-label MuiChip-labelSmall css-t3ycia-MuiChip-label">17</span></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="users" href="http://localhost:3000/admin/users" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Users</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="clients" href="http://localhost:3000/admin/clients" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Clients</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="squads" href="http://localhost:3000/admin/squads" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Teams</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="credit_assignments" href="http://localhost:3000/admin/credit_assignments" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Credit Assignments</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="actions_admin" href="http://localhost:3000/admin/actions_admin" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Actions admin</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="questionnaires" href="http://localhost:3000/admin/questionnaires" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Questionnaires</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="training_plans" href="http://localhost:3000/admin/training_plans" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Training Plans</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="squad_log_types" href="http://localhost:3000/admin/squad_log_types" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Team Log Types</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="csv_dump" href="http://localhost:3000/admin/csv_dump" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">CSV dump</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a><a class="MuiListItemButton-root MuiListItemButton-gutters MuiButtonBase-root css-n19lea-MuiButtonBase-root-MuiListItemButton-root" tabindex="0" role="button" id="generate_report" href="http://localhost:3000/admin/generate_report" target="_self"><div class="MuiListItemIcon-root css-9qa486-MuiListItemIcon-root"><svg class="MuiSvgIcon-root MuiSvgIcon-fontSizeInherit css-1cqp4q4-MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" data-testid="FiberManualRecordIcon"><circle cx="12" cy="12" r="8"></circle></svg></div><div class="MuiListItemText-root css-28royg-MuiListItemText-root"><p class="MuiTypography-root MuiTypography-body1 css-13jt4km-MuiTypography-root">Generate Report</p></div><span class="MuiTouchRipple-root css-8je8zh-MuiTouchRipple-root"></span></a></div></div></div></div>', ''),
    ]

    replace_text_in_files(folder_path, replace_list)

