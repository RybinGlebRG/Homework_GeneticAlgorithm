import lib
import evo
import packer
import requests as rq

ind1=lib.run()

Evo=evo.Evo(200)
ind2=Evo.run()

Packer=packer.Packer()

payload=Packer.pack(ind1,ind2)

response = rq.post("https://cit-home1.herokuapp.com/api/ga_homework", json=payload)
print(response.content)