import random 


eye_shape = ['round','almond','hooded','upturned','close-set','monolid','downturned','wide-set','protruding']
eye_color = ['red','orange','yellow','green','cyan','blue','violet']
hair_color = ['red','orange','yellow','green','cyan','blue','violet','black','brown','blonde','brunette']
skin_color = ['red','orange','yellow','green','cyan','blue','violet','black','brown','white']
face_shape = ['square','round','pear','oblong','oval','rectangle','triangle','diamond','heart']







class Sim:
    def create_character(eye_shape,eye_color,hair_color,skin_color,face_shape):

        cryptosim_adam = []

        eyeShape = random.choice(eye_shape)
        cryptosim_adam.append(eyeShape)
        eyeColor = random.choice(eye_color)
        cryptosim_adam.append(eyeColor)
        hairColor = random.choice(hair_color)
        cryptosim_adam.append(hairColor)
        skinColor = random.choice(skin_color)
        cryptosim_adam.append(skinColor)
        skinColor = random.choice(face_shape)
        cryptosim_adam.append(skinColor)

        print(cryptosim_adam)

        return cryptosim_adam

        


Sim.create_character(eye_shape,eye_color,hair_color,skin_color,face_shape)


