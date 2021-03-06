#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewInt class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class NewInteger(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Creates new literal value (Integer)."
        self.label = "NewInt"
        self.color = "78:87:130:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.integer",
                        "name":"interger_value",
                        "label":"Integer value",
                        "conn_type":"Output"}]
        self.group = "Basic Data Type"
        self.properties = [{"name": "integer_value",
                            "label":"Integer value",
                            "type": MOSAICODE_INT,
                            "lower": -(sys.maxint - 1),
                            "upper": sys.maxint,
                            "step": 1,
                            "value":0
                            }
                           ]


        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(integer value);
$label$_$id$_callback_t* $port[integer_value]$;
int $port[integer_value]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[integer_value]$_size ; i++){
        // Call the stored functions
        (*($port[integer_value]$[i]))($prop[integer_value]$);
    }
}
"""

# -----------------------------------------------------------------------------
