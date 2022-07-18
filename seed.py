# Seed file for sample data

from models import db, Pet
from app import app


# Drop all tables, and create them
db.drop_all()
db.create_all()


# Empty tables, just in case
Pet.query.delete()


# Sample pet photo URLs
p1_img = 'https://s36700.pcdn.co/wp-content/uploads/2019/03/Close-up-of-a-Boxer-with-tongue-out-happy-600x400.jpg.optimal.jpg'
p2_img = 'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/08/09144342/Husky-Grass.jpg'
p3_img = 'https://www.derbyshiretimes.co.uk/webimg/QVNIMTI0NjI1MTU1.jpg?width=640&quality=65&smart&enable=upscale'
p4_img = 'https://www.comfortzone.com/-/media/Images/ComfortZone-NA/US/Blog/bringing-new-kitten-home.jpg'
p5_img = 'https://t2.uc.ltmcdn.com/en/posts/9/9/9/how_to_clean_a_rabbit_cage_properly_9999_600.jpg'



# Sample pets
p1 = Pet(name='Frankie', species='dog', photo_url=p1_img, age='3', notes='Loves to play outside.')
p2 = Pet(name='Enzo', species='dog', photo_url=p2_img, age='6', notes='Great with kids, but not with cats.')
p3 = Pet(name='Wiz', species='cat', photo_url=p3_img, age='8', notes='Loves to snuggle.')
p4 = Pet(name='Toady', species='cat', photo_url=p4_img, age='1', notes='Very chatty! Enjoys watching birds.')
p5 = Pet(name='Jacko', species='rabbit', photo_url=p5_img, age='3', notes='Very partial to lettuce')


db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()
