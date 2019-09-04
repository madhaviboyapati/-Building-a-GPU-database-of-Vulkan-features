import webapp2
import jinja2
import os
import logging
from gpu_entity import GpuEntity
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class Main(webapp2.RequestHandler):


    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render({}))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        name = self.request.get("name")
        manufacturer = self.request.get("manufacturer")
        date = self.request.get("date_issued")

        gpu_key = ndb.Key('GpuEntity',name)
        current_gpu = gpu_key.get()

        if current_gpu != None:
            message = "gpu exist"

        geometry_shader = False
        if self.request.get("feature1") == "yes":
            geometry_shader = True

        logging.info(geometry_shader)

        tesselation_shader = False
        if self.request.get("feature2") == "yes":
            tesselation_shader = True

        shaderlnt_16 = False
        if self.request.get("feature3") == "yes":
            shaderlnt_16 = True

        sparse_binding = False
        if self.request.get("feature4") == "yes":
            sparse_binding = True

        texture_compressionETC2 = False
        if self.request.get("feature5") == "yes":
            texture_compressionETC2 = True


        vertex_pipeline_store_and_atomics = False
        if self.request.get("feature6") == "yes":
            vertex_pipeline_store_and_atomics = True

        newGpu = GpuEntity(id=name, name=name, manufacturer=manufacturer, geometryShader = geometry_shader,  tesselationShader = tesselation_shader,shaderInt16 = shaderlnt_16,  sparseBinding = sparse_binding,textureCompressionETC2 = texture_compressionETC2,vertexPipelineStoresAndAtomics = vertex_pipeline_store_and_atomics)
        newGpu.put()

        logging.info(name)
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render({"name": name, "message": message}))


app = webapp2.WSGIApplication([
    ('/main', Main),
], debug=True)
