from django.contrib import admin
from django.contrib.auth.models import Group, User

# Unregister the Group model
admin.site.unregister(Group)

# Unregister the default User model
admin.site.unregister(User)

# Customize the User admin interface
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login', 'is_active')  # Display username, last login, and is_active
    fields = ('username', 'email', 'password', 'is_active', 'last_login')  # Fields in the detail view
    readonly_fields = ('last_login',)  # Make the last login field read-only
    search_fields = ('username', 'email')  # Enable search by username and email
    list_filter = ('is_active',)  # Filter by is_active status

# Customize admin panel titles
admin.site.site_header = 'DRACO'
admin.site.index_title = 'Draco Dashboard'
admin.site.site_title = 'Draco ADMIN PANEL'
