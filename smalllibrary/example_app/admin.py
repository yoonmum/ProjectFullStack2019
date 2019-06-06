from django.contrib import admin
from .models import Binding, Publisher, Transaction,Book ,Borrow

# Register your models here.

@admin.register(Binding)
class BindingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Binding._meta.fields]

@admin.register(Publisher)
class Publisher(admin.ModelAdmin): 
    list_display = [f.name for f in Publisher._meta.fields]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Transaction._meta.fields]
    readonly_field = [f.name for f in Transaction._meta.fields]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Borrow._meta.fields]