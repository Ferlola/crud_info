from geopy.geocoders import Nominatim
import platform
import geocoder
import socket
import os
from urllib.request import urlopen
import re as r
import psutil
import datetime

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models



class CrudModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    update_description = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_date = models.JSONField(default=list)
    updated_times = models.IntegerField()
    location = models.JSONField(default=list)
    update_location = models.JSONField(default=list)
    machine = models.JSONField(default=list)
    update_machine = models.JSONField(default=list)
    network = models.JSONField(default=list)
    update_network = models.JSONField(default=list)
    ip = models.JSONField(default=list)
    update_ip = models.JSONField(default=list)
    hostname = models.JSONField(default=list)
    update_hostname = models.JSONField(default=list)
    IPAddr = models.JSONField(default=list)
    update_IPAddr = models.JSONField(default=list)
    ipconf = models.JSONField(default=list)
    update_ipconf = models.JSONField(default=list)
    ram_memory = models.JSONField(default=list)
    update_ram_memory = models.JSONField(default=list)
    ram_used =  models.JSONField(default=list)
    update_ram_used = models.JSONField(default=list)


    def get_network(self):
        network = platform.node()
        return network

    def getIP(self):
        d = str(urlopen('http://checkip.dyndns.com/').read())
        ip = r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
        return ip
    
    def get_host(self):
        hostname = socket.gethostname()
        return hostname
    
    def get_ipaddr(self):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        return IPAddr
    
    def get_ipconfig(self):
        ipconf =  os.system('ipconfig')
        return ipconf

    def load_location(self):
        Nomi_locator = Nominatim(user_agent="My App")
        my_location= geocoder.ip('me')
        latitude = my_location.geojson['features'][0]['properties']['lat']
        longitude = my_location.geojson['features'][0]['properties']['lng']
        location = Nomi_locator.reverse(f"{latitude}, {longitude}")
        location = location.raw['address']
        location = location['city'], location['country']
        return location

    def load_machine(self):
        plataforma = platform.freedesktop_os_release()
        machine = plataforma['PRETTY_NAME'],plataforma['ID_LIKE'],platform.machine(),platform.release()
        return machine   
    
    def get_ram_memory(self):
        ram_memory = psutil.virtual_memory()[2]
        return ram_memory
    
    def get_ram_used(self):
        ram_used = psutil.virtual_memory()[3]/1000000000
        return ram_used
    
    def save(self, *args, **kwargs):
        if not self.location:
            self.ipconf = self.get_ipconfig()
            self.IPAddr = self.get_ipaddr()
            self.hostname = self.get_host()
            self.ip = self.getIP()
            self.network = self.get_network()
            self.location = self.load_location()
            self.machine = self.load_machine()
            self.ram_memory = self.get_ram_memory()
            self.ram_used = self.get_ram_used()
            self.published_date = datetime.datetime.now()
        super(CrudModel, self).save(*args, **kwargs)   

    
    def __str__(self):
        return self.title, self.published_date    
    
@receiver(pre_save, sender=CrudModel)
def increment_integer_field(sender, instance, **kwargs):
    if not instance.pk:
        instance.updated_times = 1
    else:
        instance.updated_times += 1

                      
@receiver(pre_save, sender=CrudModel)
def update_history(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.description != instance.description:
            instance.update_description.append(old_instance.description) 
            instance.updated_date.append(old_instance.updated_at.isoformat("T", "minutes")) # check
            instance.update_location.append(old_instance.location) 
            instance.update_machine.append(old_instance.machine)
            instance.update_network.append(old_instance.network)
            instance.update_ip.append(old_instance.ip)
            instance.update_hostname.append(old_instance.hostname)
            instance.update_IPAddr.append(old_instance.IPAddr)
            instance.update_ipconf.append(old_instance.ipconf)
            instance.update_ram_memory.append(old_instance.ram_memory)
            instance.update_ram_used.append(old_instance.ram_used)
