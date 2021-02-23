# News page

## Model structure
The model consists of two classes:
1. Categories
2. News

The "Categories" model consists of 1 field
1. Category name

The "News" model consists of 5 fields:
1. Date of publication
2. News titles
3. News text
4. Main category
5. Additional categories

The `Main category` is linked to categories using a `ForeignKey`, and the `Additional category` is linked using a `ManyToManyField`.

`News titles` and `Category names` are indexed for quick search.

## Admin panel

The admin panel implements 2 classes that describe our models.
But opposed to the category, the news class uses filters by `Main category`, `Additional categories` and `Date of publication`.

### Rich text editor

In this project I am using the `Rich Text Editor` [django-tinymce](https://github.com/jazzband/django-tinymce).
