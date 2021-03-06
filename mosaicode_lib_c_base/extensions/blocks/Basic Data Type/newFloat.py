#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewFloat class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class NewFloat(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Creates new literal value (Float)."
        self.label = "NewFloat"
        self.color = "78:87:130:200"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"float_value",
                       "label":"Float value",
                       "conn_type":"Output"}]
        self.group = "Basic Data Type"
        self.properties = [{"name": "float_value",
                            "label":"Float value",
                            "type": MOSAICODE_FLOAT,
                            "lower": -(sys.float_info.max-1),
                            "upper": sys.float_info.max,
                            "step": 1.0,
                            "value":0.0}]

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[float_value]$;
int $port[float_value]$_size = 0;

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[float_value]$_size ; i++){
        // Call the stored functions
        (*($port[float_value]$[i]))($prop[float_value]$);
    }
}
"""

# -----------------------------------------------------------------------------
