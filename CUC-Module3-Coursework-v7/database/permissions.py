class Permissions:
    ADMIN = "admin"
    TEACHER = "teacher"

    def __init__(self,user):
        self.user = user
        self.permissions = {
            self.ADMIN: [
                "add_btn",
                "clear_btn",
                "update_btn",
                "delete_btn",
                "go_to_btn",
                "search_btn",
                "showall_btn",
                "search_in"
            ],
            self.TEACHER: [
                "clear_btn",
                "go_to_btn",
                "search_btn",
                "showall_btn",
                "search_in"
            ]
        }

    def check_permission(self, permission):
        return permission in self.permissions[self.user]