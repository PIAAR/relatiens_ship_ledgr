# services/human_design/human_design_interpreter.py

class HumanDesignInterpreter:
    """
    Processes raw Human Design chart data into readable summaries.
    """

    def get_type(self, chart_data):
        return chart_data.get("type", "Unknown")

    def get_authority(self, chart_data):
        return chart_data.get("authority", "Unknown")

    def get_profile(self, chart_data):
        return chart_data.get("profile", "Unknown")

    def get_defined_centers(self, chart_data):
        return chart_data.get("defined_centers", [])

    def get_open_centers(self, chart_data):
        return chart_data.get("open_centers", [])

    def get_gates(self, chart_data):
        return chart_data.get("gates", [])

    def get_channels(self, chart_data):
        return chart_data.get("channels", [])

    def summarize_design(self, type_, authority, profile, defined_centers, gates):
        centers_str = ", ".join(defined_centers) if defined_centers else "No defined centers"
        gates_str = ", ".join(str(g) for g in gates[:5]) if gates else "No gates"
        return f"You are a {type_} with {authority} authority and a {profile} profile. Your defined centers are {centers_str}. Key gates include {gates_str}."

    def summarize_composite(self, combined_data):
        theme = combined_data.get("connection_theme", "No theme description")
        centers = combined_data.get("defined_centers", [])
        open_centers = combined_data.get("open_centers", [])
        definition = combined_data.get("definition", "Unknown")

        return f"Connection theme: {theme}. Defined centers together: {', '.join(centers)}. Open centers together: {', '.join(open_centers)}. Combined definition: {definition}."
