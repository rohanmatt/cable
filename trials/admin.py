from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import User
from django  import forms
from .models import Area, Bouquet, Device, Plans, Ticket, User,Channel,Subscription,Ticket,Invoice
# Register your models here.

# admin.site.register(Area)
# admin.site.register(Device)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': ['email', 'first_name', 'last_name', 'password1', 'password2']
                        + ['pincode','phone_number','alternate_number','gst','zone','department','mpos_serial_number','mpos_user_name','area', 'assigned_devices']
            }
        ),
    )
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header

            {
                'fields': (
                    'pincode','phone_number','alternate_number','gst','zone','department','mpos_serial_number','mpos_user_name','area', 'assigned_devices',
                ),
            },
        ),
    )
admin.site.register(User,CustomUserAdmin)
admin.site.register(Area)
admin.site.register(Device)
admin.site.register(Channel)
admin.site.register(Plans)
admin.site.register(Bouquet)
admin.site.register(Subscription)
admin.site.register(Ticket)
admin.site.register(Invoice)