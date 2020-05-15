#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatDivide class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel
import sys


class FloatDivide(BlockModel):
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "base"
        self.help = "Float Divide"
        self.label = "FloatDivide"
        self.color = "103:118:54:230"
        self.ports = [{"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"input0",
                       "label":"Float value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"input1",
                       "label":"Float value",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_base.extensions.ports.float",
                       "name":"result",
                       "label":"Float value",
                       "conn_type":"Output"}]
        self.group = "Arithmetic"
        self.properties = [{"name": "input0",
                            "label":"Float value",
                            "type": MOSAICODE_FLOAT,
                            "lower": -(sys.float_info.max - 1),
                            "upper": sys.float_info.max,
                            "step": 1,
                            "value": 0},
                           {"name": "input1",
                            "label":"Float value",
                            "type": MOSAICODE_FLOAT,
                            "lower": -(sys.float_info.max - 1),
                            "upper": sys.float_info.max,
                            "step": 1,
                            "value": 1}]

        self.codes["declaration"] = \
"""
typedef void (*$label$_$id$_callback_t)(float value);
$label$_$id$_callback_t* $port[result]$;
int $port[result]$_size = 0;
float $label$_$id$_value0 = $prop[input0]$;
float $label$_$id$_value1 = $prop[input1]$;

void $port[input0]$(float value){
    $label$_$id$_value0  = value;
}

void $port[input1]$(float value){
    $label$_$id$_value1  = value;
}

void $label$_$id$_callback(void * data){
    for(int i=0 ; i < $port[result]$_size ; i++){
        // Call the stored functions
        (*($port[result]$[i]))($label$_$id$_value0 / $label$_$id$_value1);
    }
}
"""

# -----------------------------------------------------------------------------
