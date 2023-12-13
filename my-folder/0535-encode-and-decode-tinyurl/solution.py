import uuid
class Codec:
    m={}
    def getRandomString(self):
        return str(uuid.uuid4())
    random_number = random.randint(1, 62)
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key=self.getRandomString()
        while key in self.m:
            key=getRandomString()
        self.m[key]=longUrl
        print("http://tinyurl.com/"+key)
        return "http://tinyurl.com/"+key
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key=shortUrl.replace("http://tinyurl.com/","")
        print(key)
        print(self.m.get(key))
        return self.m.get(key)
        
