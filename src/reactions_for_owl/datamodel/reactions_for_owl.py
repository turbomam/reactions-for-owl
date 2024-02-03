# Auto generated from reactions_for_owl.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-02-02T19:19:34
# Schema: reactions-for-owl
#
# id: https://w3id.org/turbomam/reactions-for-owl/reactions-for-owl
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
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

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


class PlannedProcessId(NamedThingId):
    pass


class MaterialProcessingId(PlannedProcessId):
    pass


class MaterialProcessingReactionId(MaterialProcessingId):
    pass


class MaterialEntityId(NamedThingId):
    pass


class SolutionId(MaterialEntityId):
    pass


class ChemicalEntityId(MaterialEntityId):
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
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(NamedThing):
    """
    A planned process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL["PlannedProcess"]
    class_class_curie: ClassVar[str] = "reactions_for_owl:PlannedProcess"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.PlannedProcess

    id: Union[str, PlannedProcessId] = None
    has_inputs: Optional[Union[str, List[str]]] = empty_list()
    has_outputs: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, str) else str(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, str) else str(v) for v in self.has_outputs]

        super().__post_init__(**kwargs)


@dataclass
class MaterialProcessing(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL["MaterialProcessing"]
    class_class_curie: ClassVar[str] = "reactions_for_owl:MaterialProcessing"
    class_name: ClassVar[str] = "MaterialProcessing"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.MaterialProcessing

    id: Union[str, MaterialProcessingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingId):
            self.id = MaterialProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MaterialProcessingReaction(MaterialProcessing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL["MaterialProcessingReaction"]
    class_class_curie: ClassVar[str] = "reactions_for_owl:MaterialProcessingReaction"
    class_name: ClassVar[str] = "MaterialProcessingReaction"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.MaterialProcessingReaction

    id: Union[str, MaterialProcessingReactionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingReactionId):
            self.id = MaterialProcessingReactionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL["MaterialEntity"]
    class_class_curie: ClassVar[str] = "reactions_for_owl:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    has_parts: Optional[Union[str, List[str]]] = empty_list()
    part_of: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        if not isinstance(self.has_parts, list):
            self.has_parts = [self.has_parts] if self.has_parts is not None else []
        self.has_parts = [v if isinstance(v, str) else str(v) for v in self.has_parts]

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, str) else str(v) for v in self.part_of]

        super().__post_init__(**kwargs)


@dataclass
class Solution(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL["Solution"]
    class_class_curie: ClassVar[str] = "reactions_for_owl:Solution"
    class_name: ClassVar[str] = "Solution"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.Solution

    id: Union[str, SolutionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SolutionId):
            self.id = SolutionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL["ChemicalEntity"]
    class_class_curie: ClassVar[str] = "reactions_for_owl:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = REACTIONS_FOR_OWL.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.has_inputs = Slot(uri=REACTIONS_FOR_OWL.has_inputs, name="has_inputs", curie=REACTIONS_FOR_OWL.curie('has_inputs'),
                   model_uri=REACTIONS_FOR_OWL.has_inputs, domain=None, range=Optional[Union[str, List[str]]])

slots.has_outputs = Slot(uri=REACTIONS_FOR_OWL.has_outputs, name="has_outputs", curie=REACTIONS_FOR_OWL.curie('has_outputs'),
                   model_uri=REACTIONS_FOR_OWL.has_outputs, domain=None, range=Optional[Union[str, List[str]]])

slots.has_parts = Slot(uri=REACTIONS_FOR_OWL.has_parts, name="has_parts", curie=REACTIONS_FOR_OWL.curie('has_parts'),
                   model_uri=REACTIONS_FOR_OWL.has_parts, domain=None, range=Optional[Union[str, List[str]]])

slots.part_of = Slot(uri=REACTIONS_FOR_OWL.part_of, name="part_of", curie=REACTIONS_FOR_OWL.curie('part_of'),
                   model_uri=REACTIONS_FOR_OWL.part_of, domain=None, range=Optional[Union[str, List[str]]])

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=REACTIONS_FOR_OWL.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=REACTIONS_FOR_OWL.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=REACTIONS_FOR_OWL.description, domain=None, range=Optional[str])