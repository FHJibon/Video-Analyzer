def generate_report(metrics):
    return f"""
Football Clip Analysis Report

Summary:
- Average players visible per frame: {metrics['avg_players_visible']:.1f}
- Maximum players detected: {metrics['max_players_visible']}

Insights:
The clip shows active gameplay with consistent player presence.
Movement density suggests mid-field or open-play sequences.

Note:
This is an AI-assisted analysis and not an official match report.
"""