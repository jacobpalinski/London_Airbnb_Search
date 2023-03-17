from mongoengine import Document, StringField, IntField, FloatField, ListField

# Document Schema for Database
class Airbnb_Listings(Document):
    Name = StringField()
    Neighbourhood = StringField()
    Room_Type = StringField()
    Accommodates = IntField()
    Bedrooms = IntField()
    Bathrooms = IntField()
    Amenities = ListField()
    Minimum_Nights = IntField()
    Maximum_Nights = IntField()
    Price = FloatField()
    Host_Response_Time = StringField()
    Review_Score_Value = FloatField()
    Listing_Url = StringField()



