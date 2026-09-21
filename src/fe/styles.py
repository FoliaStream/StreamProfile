# src/fe/styles.py

HIDE_SIDEBAR_NAV = """
<style>
    /* Hide the default multi-page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* Make the custom sidebar navigation more prominent */
    .sidebar .sidebar-content {
        padding-top: 2rem;
    }
</style>
"""

SIDEBAR_STYLES = {
    # "container": {"padding": "1!important", "background-color": "#005B9F"}, # Blue
    "container": {"padding": "1!important", "background-color": "#fafafa"},
    "icon": {"color": "#EAA300", "font-size": "24px"}, # Darker Orange
    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#E6F0FA", "color": "#005B9F"},
    "nav-link-selected": {"background-color": "#EAA300", "color": "#005B9F"} # Darker Orange selected state on blue
}

# --- NEW: Paste your exact card styles here ---
CARD_STYLES = """
<style>
.custom-card {
    background-color: #fafafa;
    border-left: 5px solid #005B9F; /* Blue border */
    padding: 0.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    text-align: justify; 
    height: 300px; 
    overflow-y: auto;
}
.custom-card h3 {
    color: #005B9F; /* Blue heading */
    margin-top: 0;
    margin-bottom: 0.5rem;
    font-size: 1.25rem;
    text-align: justify; 
}
.custom-card .date {
    color: #EAA300; /* Darker Orange date */
    font-weight: bold;
    font-size: 1.25rem;
    margin-bottom: 0.3rem;
    margin-top: 0.8rem;
    text-align: justify; 
}
.custom-card p {
    color: #333;
    font-size: 0.9rem;
    line-height: 1.4;
    margin-bottom: 0.5rem;
    text-align: justify; 
}
.custom-card a {
    color: #005B9F; /* Darker Orange link */
    text-decoration: none;
    font-weight: bold;
    font-size: 0.9rem;
    display: inline-block;
    margin-top: 0.5rem;
    text-align: justify; 
}
.custom-card a:hover {
    text-decoration: underline;
}


.custom-card-home {
    background-color: #fafafa;
    border-left: 5px solid #005B9F; /* Blue border */
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    text-align: justify; 
    height: 370px; 
    overflow-y: auto;
}
.custom-card-home h3 {
    color: #005B9F; /* Blue heading */
    margin-top: 0;
    margin-bottom: 0.5rem;
    font-size: 1.25rem;
    text-align: justify; 
}
.custom-card-home .date {
    color: #EAA300; /* Darker Orange date */
    font-weight: bold;
    font-size: 0.85rem;
    margin-bottom: 0.3rem;
    margin-top: 0.8rem;
    text-align: justify; 
}
.custom-card-home .extra {
    color: #005B9F; 
    font-weight: bold;
    font-size: 1.2rem;
    margin-bottom: 0.3rem;
    margin-top: 0.8rem;
    text-align: justify; 
}
.custom-card-home p {
    color: #333;
    font-size: 0.9rem;
    line-height: 1.4;
    margin-bottom: 0.5rem;
    text-align: justify; 
}
.custom-card-home a {
    color: #EAA300; /* Darker Orange link */
    text-decoration: none;
    font-weight: bold;
    font-size: 0.9rem;
    display: inline-block;
    margin-top: 0.5rem;
    text-align: justify; 
}
.custom-card-home a:hover {
    text-decoration: underline;
}






/* Specific styling for the Personal Info card */
.info-card {
    background-color: #fafafa;
    border-left: 5px solid #EAA300; /* Orange border for info */
    padding: 2rem;
    border-radius: 0.5rem;
    margin-bottom: 2rem;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
}
.info-card h1 {
    color: #005B9F;
    margin-bottom: 0.5rem;
}
.info-card .details {
    font-size: 1.05rem;
    line-height: 1.6;
    color: #333;
    text-align: justify; 
}
.info-card .details a {
    color: #EAA300;
    text-decoration: none;
    font-weight: bold;
}
.info-card .details a:hover {
    text-decoration: underline;
}
</style>
"""