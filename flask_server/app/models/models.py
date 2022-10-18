from sqlalchemy import UniqueConstraint
from sqlalchemy.types import JSON

from app import db, ma

# Define Models
# Models for variables data
class variavel_independente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)

    # create A String
    def __repr__(self):
        return "<Name: %r, Description: %r>" % (self.name, self.description)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_json(self):
        return {"id": self.id, "name": self.name, "description": self.description}


class variavel_dependente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)

    # create A String
    def __repr__(self):
        return "<Name: %r, Description: %r>" % (self.name, self.description)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_json(self):
        return {"id": self.id, "name": self.name, "description": self.description}


class metrica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    # create A String

    def __repr__(self):
        return "<name: %r>" % (self.name)

    def __init__(self, name, description):
        self.name = name
        self.description = description



class referencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referencia = db.Column(db.String(500), nullable=False, unique=True)

    # create A String
    def __repr__(self):
        return "<referencia: %r>" % (self.referencia)

    def __init__(self, referencia):
        self.referencia = referencia

    def to_json(self):
        return {"id": self.id, "referencia": self.referencia}


class referencia_vi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_vi = db.Column(db.Integer, nullable=False)
    id_ref = db.Column(db.Integer, nullable=False)
    __table_args__ = (UniqueConstraint('id_vi', 'id_ref', name='uc_vi_ref'),
                      )

    def __init__(self, id_vi, id_ref):
        self.id_vi = id_vi
        self.id_ref = id_ref

    def to_json(self):
        return {"id": self.id, "id_vi": self.id_vi, "id_ref": self.id_ref}


class referencia_vd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_vd = db.Column(db.Integer, nullable=False)
    id_ref = db.Column(db.Integer, nullable=False)
    __table_args__ = (UniqueConstraint('id_vd', 'id_ref', name='uc_vd_ref'),
                      )

    def __init__(self, id_vd, id_ref):
        self.id_vd = id_vd
        self.id_ref = id_ref

    def to_json(self):
        return {"id": self.id, "id_vd": self.id_vd, "id_ref": self.id_ref}


class referencia_metrica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_metric = db.Column(db.Integer, nullable=False)
    id_ref = db.Column(db.Integer, nullable=False)
    __table_args__ = (UniqueConstraint('id_metric', 'id_ref', name='uc_metric_ref'),
                      )

    def __init__(self, id_metric, id_ref):
        self.id_metric = id_metric
        self.id_ref = id_ref


class design_vi_vd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_vi = db.Column(db.Integer, nullable=False)
    id_vd_array = db.Column(db.String(100), nullable=False)
    __table_args__ = (UniqueConstraint('id_vi', 'id_vd_array', name='uc_vi_vd'),
                      )

    def __init__(self, id_vi, id_vd_array):
        self.id_vi = id_vi
        self.id_vd_array = id_vd_array

    def to_json(self):
        return {"id": self.id, "id_vi": self.id_vi, "id_vd_array": self.id_vd_array}


class VariableSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')


variable_schema = VariableSchema()
variables_schema = VariableSchema(many=True)


class MetricSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')


metric_schema = MetricSchema()
metrics_schema = MetricSchema(many=True)


class ReferenceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'referencia')


reference_schema = ReferenceSchema()
references_schema = ReferenceSchema(many=True)


class ViReferenceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_vi', 'id_ref')


vi_reference_schema = ViReferenceSchema()
vi_references_schema = ViReferenceSchema(many=True)


class VdReferenceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_vd', 'id_ref')


vd_reference_schema = VdReferenceSchema()
vd_references_schema = VdReferenceSchema(many=True)


class MetricReferenceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_metric', 'id_ref')


metric_reference_schema = MetricReferenceSchema()
metric_references_schema = MetricReferenceSchema(many=True)


class ViVdSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_vi', 'id_vd_array')


vi_vd_schema = ViVdSchema()
vi_vds_schema = ViVdSchema(many=True)
