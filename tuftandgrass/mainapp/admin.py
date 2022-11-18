from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class NoAddNoDelete(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class IndexPageAdmin(NoAddNoDelete):
    fields = (
        (
            'title_ru',
            'title_uz',
            'title_en',
            'description_ru',
            'description_uz',
            'description_en',
        ),
        (
            'facebook',
            'youtube',
            'telegram',
            'phone',
            'address_ru',
            'address_uz',
            'address_en',
            'worktime_ru',
            'worktime_uz',
            'worktime_en',
        ),
        (
            'secondblock_img',
            'secondblock_link',
            'secondblock_title_ru',
            'secondblock_title_en',
            'secondblock_title_uz',
            'secondblock_subtitle_ru',
            'secondblock_subtitle_en',
            'secondblock_subtitle_uz',
            'secondblock_description_ru',
            'secondblock_description_en',
            'secondblock_description_uz',
            'secondblock_feature_1_ru',
            'secondblock_feature_1_en',
            'secondblock_feature_1_uz',
            'secondblock_feature_2_ru',
            'secondblock_feature_2_en',
            'secondblock_feature_2_uz',
            'secondblock_feature_3_ru',
            'secondblock_feature_3_en',
            'secondblock_feature_3_uz',
            'secondblock_feature_4_ru',
            'secondblock_feature_4_en',
            'secondblock_feature_4_uz',
            'secondblock_feature_5_ru',
            'secondblock_feature_5_en',
            'secondblock_feature_5_uz',
            'secondblock_feature_6_ru',
            'secondblock_feature_6_en',
            'secondblock_feature_6_uz',
        ),
        (
            'thirdblock_title_ru',
            'thirdblock_title_en',
            'thirdblock_title_uz',
            'thirdblock_description_ru',
            'thirdblock_description_en',
            'thirdblock_description_uz',
        ),
        (
            'fourthblock_img',
            'fourthblock_title_ru',
            'fourthblock_title_en',
            'fourthblock_title_uz',
            'fourthblock_description_ru',
            'fourthblock_description_en',
            'fourthblock_description_uz',
        ),
        (
            'fifthblock_title_ru',
            'fifthblock_title_en',
            'fifthblock_title_uz',
            'fifthblock_description_ru',
            'fifthblock_description_en',
            'fifthblock_description_uz',
        ),
        (
            'eighthblock_title_ru',
            'eighthblock_title_en',
            'eighthblock_title_uz',
            'eighthblock_description_ru',
            'eighthblock_description_en',
            'eighthblock_description_uz',
        ),
        (
            'ninthblock_title_ru',
            'ninthblock_title_en',
            'ninthblock_title_uz',
            'ninthblock_description_ru',
            'ninthblock_description_en',
            'ninthblock_description_uz',
        ),
        'copyright_ru',
        'copyright_en',
        'copyright_uz',
    )


class NewsListPageAdmin(NoAddNoDelete):
    fields = (
        'title_ru',
        'title_en',
        'title_uz',
        'description_ru',
        'description_en',
        'description_uz',
    )


class IndexPageSlideAdmin(admin.ModelAdmin):
    fields = (
        'img',
        'link',
        (
            'first_title_ru',
            'first_title_en',
            'first_title_uz',
            'second_title_ru',
            'second_title_en',
            'second_title_uz',
        ),
        'description_ru',
        'description_en',
        'description_uz',
    )


class IndexPageProductAdmin(admin.ModelAdmin):
    fields = (
        'img',
        'link',
        'title_ru',
        'title_en',
        'title_uz',
        'description_ru',
        'description_en',
        'description_uz',
    )


class IndexPageFAQAdmin(admin.ModelAdmin):
    fields = (
        'question_ru',
        'question_en',
        'question_uz',
        'answer_ru',
        'answer_en',
        'answer_uz',
    )


class IndexPageTeamUnitAdmin(admin.ModelAdmin):
    fields = (
        'img',
        'name_ru',
        'name_en',
        'name_uz',
        'position_ru',
        'position_en',
        'position_uz',
        'description_ru',
        'description_en',
        'description_uz',
        'facebook',
        'instagram',
        'telegram',
    )


class OrderAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return False

    fields = (
        'name',
        'phone',
        'email',
        'text',
    )


class ReviewAdmin(admin.ModelAdmin):
    fields = (
        'img',
        'name_ru',
        'name_en',
        'name_uz',
        'position_ru',
        'position_en',
        'position_uz',
        'text_ru',
        'text_en',
        'text_uz',
    )


class NewsAdmin(SummernoteModelAdmin):
    fields = (
        'title_ru',
        'title_en',
        'title_uz',
        'description_ru',
        'description_en',
        'description_uz',
        'img',
        'date',
        'text_ru',
        'text_en',
        'text_uz',
    )
    summernote_fields = (
        'text_ru',
        'text_en',
        'text_uz',
    )


class HeaderAdmin(NoAddNoDelete):
    fields = (
        'img',
    )


class FooterAdmin(NoAddNoDelete):
    fields = (
        'img',
        'description_ru',
        'description_en',
        'description_uz',
        (
            'address_ru',
            'address_en',
            'address_uz',
            'phone',
            'mail',
            'website',
        ),
        (
            'mail_description_ru',
            'mail_description_en',
            'mail_description_uz',
        ),
        (
            'facebook',
            'instagram',
            'telegram',
            'youtube',
        ),
    )


class SubscribeAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return False

    fields = (
        'email',
    )


class CategoryListPageAdmin(NoAddNoDelete):
    fields = (
        'title_ru',
        'title_en',
        'title_uz',
        'description_ru',
        'description_en',
        'description_uz',
    )


class CategoryAdmin(admin.ModelAdmin):
    fields = (
        'img',
        'title_ru',
        'title_en',
        'title_uz',
        'description_ru',
        'description_en',
        'description_uz',
        'slug',
    )
    prepopulated_fields = {"slug": ("title_en",)}


class SubCategoryAdmin(admin.ModelAdmin):
    fields = (
        'img',
        'title_ru',
        'title_en',
        'title_uz',
        'category',
        'price',
        'slug',
    )
    prepopulated_fields = {"slug": ("title_en",)}


class ProductImageInline(admin.StackedInline):
    model = ProductImageModel


class ProductSpecificationInline(admin.StackedInline):
    model = ProductSpecificationModel


class ProductAdmin(admin.ModelAdmin):
    fields = (
        'img',
        'title_ru',
        'title_en',
        'title_uz',
        'description_ru',
        'description_en',
        'description_uz',
        'subcategory',
        'price',
        'new',
        'available',
        'slug',
    )
    prepopulated_fields = {"slug": ("title_en",)}
    inlines = [
        ProductImageInline,
        ProductSpecificationInline,
    ]


class AboutPageAdmin(NoAddNoDelete):
    fields = (
        'title_ru',
        'title_en',
        'title_uz',
        'description_ru',
        'description_en',
        'description_uz',
    )


class ContactsPageAdmin(NoAddNoDelete):
    fields = (
        'title_ru',
        'title_en',
        'title_uz',
        'description_ru',
        'description_en',
        'description_uz',
    )


admin.site.register(IndexPageModel, IndexPageAdmin)
admin.site.register(NewsListPageModel, NewsListPageAdmin)
admin.site.register(IndexPageSlideModel, IndexPageSlideAdmin)
admin.site.register(IndexPageProductModel, IndexPageProductAdmin)
admin.site.register(IndexPageFAQModel, IndexPageFAQAdmin)
admin.site.register(IndexPageTeamUnitModel, IndexPageTeamUnitAdmin)
admin.site.register(OrderModel, OrderAdmin)
admin.site.register(ReviewModel, ReviewAdmin)
admin.site.register(NewsModel, NewsAdmin)
admin.site.register(HeaderModel, HeaderAdmin)
admin.site.register(FooterModel, FooterAdmin)
admin.site.register(SubscribeModel, SubscribeAdmin)
admin.site.register(CategoryListPageModel, CategoryListPageAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(SubCategoryModel, SubCategoryAdmin)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(AboutPageModel, AboutPageAdmin)
admin.site.register(ContactsPageModel, ContactsPageAdmin)
