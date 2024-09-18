from template_maker import entity_maker, da_maker


# entity_maker("Car", ["id", "name", "model", "plate"])
# da_maker("Car", ["id", "name", "model", "plate"])
#
# entity_maker("Course", ["id", "title", "department"])
# da_maker("Course", ["id", "title", "department"])

entity_maker("Bill", ["date", "id", "book_name"])
da_maker("Bill", ["date", "id", "book_name"])