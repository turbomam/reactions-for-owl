# Auto generated from reactions_for_owl.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-02-02T10:37:41
# Schema: reactions-for-owl
#
# id: https://w3id.org/turbomam/reactions-for-owl
# description: Iterative, OWL-friendly model of proteolytic reactions
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
REACTIONS_FOR_OWL = CurieNamespace('reactions_for_owl', 'https://w3id.org/turbomam/reactions-for-owl/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = REACTIONS_FOR_OWL


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class PersonId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.NamedThing

    id: Union[str, NamedThingId] = None
    has_qualified_identifiers: Optional[Union[Union[dict, "QualifiedIdentifier"], List[Union[dict, "QualifiedIdentifier"]]]] = empty_list()
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if not isinstance(self.has_qualified_identifiers, list):
            self.has_qualified_identifiers = [self.has_qualified_identifiers] if self.has_qualified_identifiers is not None else []
        self.has_qualified_identifiers = [v if isinstance(v, QualifiedIdentifier) else QualifiedIdentifier(**as_dict(v)) for v in self.has_qualified_identifiers]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    Represents a Person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL["Person"]
    class_class_curie: ClassVar[str] = "reactions_for_owl:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass
class PersonCollection(YAMLRoot):
    """
    A holder for Person objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL["PersonCollection"]
    class_class_curie: ClassVar[str] = "reactions_for_owl:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.PersonCollection

    entries: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class QualifiedIdentifier(YAMLRoot):
    """
    A non-NMDC identifier for something that is also present in the NMDC database. Provides support for saying when
    the identifier was asserted and assessments about the quality of the identifier.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["QualifiedIdentifier"]
    class_class_curie: ClassVar[str] = "linkml:QualifiedIdentifier"
    class_name: ClassVar[str] = "QualifiedIdentifier"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.QualifiedIdentifier

    external_identifier_value: Optional[Union[str, URIorCURIE]] = None
    provenance: Optional[str] = None
    assertion_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.external_identifier_value is not None and not isinstance(self.external_identifier_value, URIorCURIE):
            self.external_identifier_value = URIorCURIE(self.external_identifier_value)

        if self.provenance is not None and not isinstance(self.provenance, str):
            self.provenance = str(self.provenance)

        if self.assertion_date is not None and not isinstance(self.assertion_date, str):
            self.assertion_date = str(self.assertion_date)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=REACTIONS_FOR_OWL.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=REACTIONS_FOR_OWL.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=REACTIONS_FOR_OWL.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=REACTIONS_FOR_OWL.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=REACTIONS_FOR_OWL.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=REACTIONS_FOR_OWL.age_in_years, name="age_in_years", curie=REACTIONS_FOR_OWL.curie('age_in_years'),
                   model_uri=REACTIONS_FOR_OWL.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=REACTIONS_FOR_OWL.vital_status, name="vital_status", curie=REACTIONS_FOR_OWL.curie('vital_status'),
                   model_uri=REACTIONS_FOR_OWL.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.external_identifier_value = Slot(uri=REACTIONS_FOR_OWL.external_identifier_value, name="external_identifier_value", curie=REACTIONS_FOR_OWL.curie('external_identifier_value'),
                   model_uri=REACTIONS_FOR_OWL.external_identifier_value, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.provenance = Slot(uri=REACTIONS_FOR_OWL.provenance, name="provenance", curie=REACTIONS_FOR_OWL.curie('provenance'),
                   model_uri=REACTIONS_FOR_OWL.provenance, domain=None, range=Optional[str])

slots.assertion_date = Slot(uri=REACTIONS_FOR_OWL.assertion_date, name="assertion_date", curie=REACTIONS_FOR_OWL.curie('assertion_date'),
                   model_uri=REACTIONS_FOR_OWL.assertion_date, domain=None, range=Optional[str])

slots.has_qualified_identifiers = Slot(uri=REACTIONS_FOR_OWL.has_qualified_identifiers, name="has_qualified_identifiers", curie=REACTIONS_FOR_OWL.curie('has_qualified_identifiers'),
                   model_uri=REACTIONS_FOR_OWL.has_qualified_identifiers, domain=None, range=Optional[Union[Union[dict, QualifiedIdentifier], List[Union[dict, QualifiedIdentifier]]]])

slots.personCollection__entries = Slot(uri=REACTIONS_FOR_OWL.entries, name="personCollection__entries", curie=REACTIONS_FOR_OWL.curie('entries'),
                   model_uri=REACTIONS_FOR_OWL.personCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.Person_primary_email = Slot(uri=SCHEMA.email, name="Person_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=REACTIONS_FOR_OWL.Person_primary_email, domain=Person, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))