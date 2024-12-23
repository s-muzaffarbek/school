from django.contrib import admin
from .models import CustomUser, Subject, Test, StudentResult, Classroom
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Adjust the fieldsets to ensure no duplicates
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'middle_name', 'image')}),
        # ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        # ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role & Classroom', {'fields': ('role', 'classroom')}),  # Make sure fields are unique here
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('role', 'username', 'password1', 'password2', 'email', 'first_name','last_name', 'middle_name','image','classroom'),
        }),
    )
    search_fields = ('username', 'email',)
    ordering = ('username',)



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ('id','name', 'get_users')
    search_fields = ('name',)
    list_filter = ('name',)

    def get_users(self, obj):
        return ", ".join([user.username for user in obj.user.all()])

    get_users.short_description = 'Users'

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    model = Classroom
    list_display = ('id','name', 'get_users')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_filter = ('name',)

    def get_users(self, obj):
        return ", ".join([user.username for user in obj.classroom.all()])

    get_users.short_description = 'Users'

@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    model = StudentResult
    list_display = ('id', 'get_class', 'student', 'subject', 'total_questions', 'correct_answers', 'incorrect_answers', 'time',)
    list_display_links = ('id',)
    search_fields = ('student__username',)
    list_filter = ('subject',)

    def get_class(self, obj):
        return ", ".join([classroom.name for classroom in obj.student.classroom.all()])

    get_class.short_description = 'Class'

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    model = Test
    list_display = ('id', 'subject')
    list_display_links = ('id',)
    search_fields = ('student__username',)
    list_filter = ('subject',)

    def get_class(self, obj):
        return ", ".join([classroom.name for classroom in obj.student.classroom.all()])

    get_class.short_description = 'Class'