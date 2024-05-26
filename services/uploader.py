class Uploader:


    @staticmethod
    def car_image_uploader(instance, filename):
        return f"car/{instance.car.model}/{filename}"
    
    @staticmethod
    def location_image_uploader(instance, filename):
        return f"location/{instance.location.country.name}/{filename}"
    
    @staticmethod
    def additional_image_uploader(instance, filename):
        return f"additional/{instance.icon}/{filename}"
    
    @staticmethod
    def house_image_uploader(instance, filename):
        return f"house/{instance.house.rooms}/{filename}"
    
    @staticmethod
    def category_image_uploader(instance, filename):
        return f"category/{instance.name}/{filename}"
    
    @staticmethod
    def notification_image_uploader(instance, filename):
        return f"notifications/{instance.user.email}/{filename}"
    
    @staticmethod
    def news_image_uploader(instance, filename):
        return f"news/{instance.news}/{filename}"
    
    @staticmethod
    def event_image_uploader(instance, filename):
        return f"event/{instance.event}/{filename}"
    
    @staticmethod
    def event_additional_uploader(instance, filename):
        return f"additonal/{instance.icon}/{filename}"
    

    

    