""" This Module Contains the Syntax of C-Grass Plus """

cfg = {
    "<program>" : "seed <import> <global> garden() (<statement>); <function> plant",
    "<import>" : ["transplant #identifier; <import>", "EPSILON"],
    "<global>" : ["floral #identifier; <global>", "EPSILON"],
    "<statement>" : [
                     "<local-variable>; <statement>", "<i/o-statement>; <statement>", 
                     "<assignment>; <statement>", 
                     "leaf (<condition>) (<statement>); <more-condition> <else>; <statement>", 
                     "<iterative>; <statement>", "<math>; <statement>", 
                     "#identifier (<argument>) <statement>", 
                     "clear; <statement>", "break;", "EPSILON"
                    ],
    "<local-variable>" : [
                     "tint #identifier <tint-value> <more-tint>",
                     "flora #identifier <flora-value> <more-flora>",
                     "chard #identifier <chard-value> <more-chard>",
                     "string #identifier <string-value> <more-string>",
                     "bloom #identifier <bloom-value> <more-bloom>",
                     "florist #identifier <florist-value> <more-florist>",
                     "tulip #identifier <tulip-stem-value> <more-tulip-stem>",
                     "dirt #identifier <dirt-value> <more-dirt>",
                     "stem #identifier <tulip-stem-value> <more-tulip-stem>"
                        ],
    "<tint-value>" : ["= <tint>", "EPSILON"],
    "<flora-value>" : ["= <flora>", "EPSILON"],
    "<chard-value>" : ["= <chard>", "EPSILON"],
    "<string-value>" : ["= <string>", "EPSILON"],
    "<bloom-value>" : ["= <bloom>", "EPSILON"],
    "<florist-value>" : ["= [<all-value> <more-value>]", "EPSILON"],
    "<tulip-stem-value>" : ["= {<all-value> <more-value>}", "EPSILON"],
    "<dirt-value>" : ["= {<dirt>}", "EPSILON"],
    "<tint>" : ["tint literal", "#identifier"],
    "<flora>" : ["flora literal", "#identifier"],
    "<chard>" : ["chard literal", "#identifier"],
    "<string>" : ["string literal", "#identifier"],
    "<bloom>" : ["bloom literal", "#identifier"],
    "<dirt>" : ["string literal: [<all-value> <more-value>] <more-pair-value>", "#identifier"],
    "<numeric>" : ["tint literal", "flora literal", "#identifier"],
    "<all-value>" : [
                    "<numeric>", "chard literal", "string literal",
                    "bloom literal", "bare", "[<all-value> <more-value>] <index>",
                    "{<all-value> <more-value>} <index", "{<dirt>} <dirt-key> <index>"
                    ],
    "<more-value>" : [", <all-value> <more-value>", "EPSILON"],
    "<more-pair-value>" : [", <dirt>", "EPSILON"],
    "<index>" : ["[tint literal] <index>", "EPSILON"],
    "<dirt-key>" : ["[string literal] <index> <dirt-key>", "EPSILON"],
    "<more-tint>" : [", #identifier <tint-value> <more-tint>", "EPSILON"],
    "<more-flora>" : [", #identifier <flora-value> <more-flora>", "EPSILON"],
    "<more-chard>" : [", #identifier <chard-value> <more-chard>", "EPSILON"],
    "<more-string>" : [", #identifier <string-value> <more-string>", "EPSILON"],
    "<more-bloom>" : [", #identifier <bloom-value> <more-bloom>", "EPSILON"],
    "<more-florist>" : [", #identifier <florist-value> <more-florist>", "EPSILON"],
    "<more-tulip-stem>" : [", #identifier <tulip-stem-value> <more-tulip-stem>", "EPSILON"],
    "<more-dirt>" : [", #identifier <dirt-value> <more-dirt>", "EPSILON"],
    "<i/o-statement>" : ["<inpetal-receiver> inpetal (string literal)", "mint (<mint-entry>)"],
    "<inpetal-receiver>" : [
                            "<datatype> #identifier =", "florist #identifier =",
                            "tulip #identifier =", "dirt #identifier =", "stem #identifier =",
                            "#identifier =", "EPSILON"
                            ],
    "<datatype>" : ["tint", "flora", "chard", "string", "bloom"],
    "<mint-entry>" : ["<all-value>", "<math>", "EPSILON"],
    "<math>" : ["<numeric> <start-operation>", "(<numeric> <start-operation>)", "<string> <concatenate>"],
    "<start-operation>" : ["<operator> <start-operation>", "(<operator> <start-operation>)", "EPSILON"],
    "<operator>" : [
                    "+ <numeric>", "- <numeric>",
                    "* <numeric>", "/ <numeric>",
                    "% <numeric>", "** <numeric>",
                    "// <numeric>", "EPSILON"
                    ],
    "<concatenate>" : ["+ <string> <concatenate>", "EPSILON"],
    "<assignment>" : [
                    "<numeric> <assignment-op> <numeric>",
                    "#identifier <equals-plus> <math>",
                    "<string> <equals-plus> <all-value>"
                    ],
    "<assignment-op>" : ["<equals-plus>", "-=", "*=", "/=", "%=", "**=", "//="],
    "<equals-plus>" : ["=", "+="],
    "<condition>" : ["<numeric> <numeric-condition>", "<all-value> <string-condition>"],
    "<numeric-condition>" : ["<numeric-cond-op> <numeric>", "EPSILON"],
    "<string-condition>" : ["<string-cond-op> <all-value>", "EPSILON"],
    "<numeric-cond-op>" : ["<string-cond-op>", ">", "<", ">=", "<="],
    "<string-cond-op>" : ["==", "!=", "=&", "=/"],
    "<more-condition>" : ["eleaf (<condition>) (<statement>); <more-condition>"],
    "<else>" : ["moss (<statement>)"],
    "<iterative>" : [
            "fern (tint #identifier = <tint>; #identifier <numeric-cond-op> <tint>; #identifier <assignment-op> <tint>) (<statement>)",
            "willow (<condition>) (<statement>)"
            ],
    "<argument>" : ["<all-value> <add-argument>", "EPSILON"],
    "<add-argument>" : [", <argument>", "EPSILON"],
    "<function>" : [
                    "<datatype> #identifier (<parameter>) (<statement> regrow <all-value>;); <function>",
                    "viola #identifier() (<statement>); <function>",
                    "EPSILON"
                    ],
    "<parameter>" : ["<local-variable> <add-parameter>", "EPSILON"],
    "<add-parameter>" : [", <parameter>", "EPSILON"]
}

first_set = {
    "<program>" : ["seed"],
    "<import>" : ["transplant", "EPSILON"],
    "<global>" : ["floral", "EPSILON"],
    "<statement>" : [
                    "tint", "flora", "chard",
                    "string", "bloom", "florist",
                    "tulip", "dirt", "stem", "#",
                    "inpetal", "mint", "tint literal",
                    "flora literal", "leaf", "fern",
                    "willow", "(", "string literal",
                    "clear", "break", "EPSILON"
                    ],
    "<local-variable>" : [
                        "tint", "flora", "chard",
                        "string", "bloom", "florist",
                        "tulip", "dirt", "stem"
                        ],
    "<tint-value>" : ["=", "EPSILON"],
    "<flora-value>" : ["=", "EPSILON"],
    "<chard-value>" : ["=", "EPSILON"],
    "<string-value>" : ["=", "EPSILON"],
    "<bloom-value>" : ["=", "EPSILON"],
    "<florist-value>" : ["=", "EPSILON"],
    "<tulip-stem-value>" : ["=", "EPSILON"],
    "<dirt-value>" : ["=", "EPSILON"],
    "<tint>" : ["tint literal", "#"],
    "<flora>" : ["flora literal", "#"],
    "<chard>" : ["chard literal", "#"],
    "<string>" : ["string literal", "#"],
    "<bloom>" : ["bloom literal", "#"],
    "<dirt>" : ["string literal", "#"],
    "<numeric>" : ["tint literal", "flora literal", "#"],
    "<all-value>" : [
                    "tint literal", "flora literal",
                    "#", "chard literal", "string literal",
                    "bloom literal", "bare", "[", "{"
                    ],
    "<more-value>" : [",", "EPSILON"],
    "<more-pair-value>" : [",", "EPSILON"],
    "<index>" : ["[", "EPSILON"],
    "<dirt-key>" : ["[", "EPSILON"],
    "<more-tint>" : [",", "EPSILON"],
    "<more-flora>" : [",", "EPSILON"],
    "<more-chard>" : [",", "EPSILON"],
    "<more-string>" : [",", "EPSILON"],
    "<more-bloom>" : [",", "EPSILON"],
    "<more-florist>" : [",", "EPSILON"],
    "<more-tulip-stem>" : [",", "EPSILON"],
    "<more-dirt>" : [",", "EPSILON"],
    "<i/o-statement>" : [
                        "tint", "flora", "chard",
                        "string", "bloom", "florist",
                        "tulip", "dirt", "stem",
                        "#", "inpetal", "mint"
                        ],
    "<inpetal-receiver>" : [
                            "tint", "flora", "chard",
                            "string", "bloom", "florist",
                            "tulip", "dirt", "stem",
                            "#", "EPSILON"
                            ],
    "<datatype>" : ["tint", "flora", "chard", "string", "bloom"],
    "<mint-entry>" : [
                    "tint literal", "flora literal", "#",
                    "chard literal", "string literal", "bloom literal",
                    "bare", "[", "{", "(", "EPSILON"
                    ],
    "<math>" : ["tint literal", "flora literal", "#", "(", "string literal"],
    "<start-operation>" : ["+", "-", "*", "/", "%", "(", "EPSILON"],
    "<operator>" : ["+", "-", "*", "/", "%", "EPSILON"],
    "<concatenate>" : ["+", "EPSILON"],
    "<assignment>" : ["tint literal", "flora literal", "#"],
    "<assignment-op>" : ["=", "+", "-", "*", "/", "%"],
    "<equals-plus>" : ["=", "+"],
    "<condition>" : [
                    "tint literal", "flora literal",
                    "#", "chard literal", "string literal",
                    "bloom literal", "bare", "[", "{"
                    ],
    "<numeric-condition>" : ["=", "!", ">", "<", "EPSILON"],
    "<string-condition>" : ["=", "!", "EPSILON"],
    "<numeric-cond-op>" : ["=", "!", ">", "<"],
    "<string-cond-op>" : ["=", "!"],
    "<more-condition>" : ["eleaf", "EPSILON"],
    "<else>" : ["moss", "EPSILON"],
    "<iterative>" : ["fern", "willow"],
    "<argument>" : [
                    "tint literal", "flora literal", "#",
                    "chard literal", "string literal", "bloom literal",
                    "bare", "[", "{", "EPSILON"
                    ],
    "<add-argument>" : [",", "EPSILON"],
    "<function>" : [
                    "tint", "flora", "chard",
                    "string", "bloom",
                    "viola", "EPSILON"
                    ],
    "<parameter>" : [
                    "tint", "flora", "chard",
                    "string", "bloom", "florist",
                    "tulip", "dirt", "stem", "EPSILON"
                    ],
    "<add-parameter>" : [",", "EPSILON"]
    }

follow_set = {
    "<program>" : "$",
    "<import>" : ["floral", "garden"],
    "<global>" : "garden",
    "<statement>" : [")", "regrow"],
    "<local-variable>" : [";", ",", "$", ")"],
    "<tint-value>" : [",", "$", ";", ")"],
    "<flora-value>" : [",", "$", ";", ")"],
    "<chard-value>" : [",", "$", ";", ")"],
    "<string-value>" : [",", "$", ";", ")"],
    "<bloom-value>" : [",", "$", ";", ")"],
    "<florist-value>" : [",", "$", ";", ")"],
    "<tulip-stem-value>" : [",", "$", ";", ")"],
    "<dirt-value>" : [",", "$", ";", ")"],
    "<tint>" : [",", "$", ";", ")"],
    "<flora>" : [",", "$", ";", ")"],
    "<chard>" : [",", "$", ";", ")"],
    "<string>" : [",", "$", "+", ";", ")"],
    "<bloom>" : [",", "$", ";", ")"],
    "<dirt>" : ["}"],
    "<numeric>" : [
                ",", "]", "}", ")",
                ";", "=", "!", "+",
                "-", "*", "/", "%",
                "(", ">", "<"
                ],
    "<all-value>" : [",", "]", "}", ")", ";", "=", "!"],
    "<more-value>" : ["]", "}"],
    "<more-pair-value>" : "}",
    "<index>" : [",", "]", "}", ")", ";", "=", "!", "["],
    "<dirt-key>" : ["[", ",", "]", "}", ")", ";", "=", "!"],
    "<more-tint>" : [";", ",", "$", ")"],
    "<more-flora>" : [";", ",", "$", ")"],
    "<more-chard>" : [";", ",", "$", ")"],
    "<more-bloom>" : [";", ",", "$", ")"],
    "<more-florist>" : [";", ",", "$", ")"],
    "<more-tulip-stem>" : [";", ",", "$", ")"],
    "<more-dirt>" : [";", ",", "$", ")"],
    "<i/o-statement>" : ";",
    "<inpetal-receiver>" : "inpetal",
    "<datatype>" : "#",
    "<mint-entry>" : ")",
    "<math>" : [";", ")"],
    "<start-operation>" : [";", ")"],
    "<operator>" : ["(", "$", ";", ")"],
    "<concatenate>" : [";", ")"],
    "<assignment>" : ";",
    "<assignment-op>" : ["tint literal", "flora literal", "#"],
    "<equals-plus>" : [
                        "tint literal", "flora literal", "#",
                        "chard literal", "string literal",
                        "bloom literal", "bare",
                        "[", "{", "("
                      ],
    "<condition>" : ")",
    "<numeric-condition>" : ")",
    "<string-condition>" : ")",
    "<numeric-cond-op>" : ["tint literal", "flora literal", "#"],
    "<string-cond-op>" : [
                            "tint literal", "flora literal", "#",
                            "chard literal", "string literal",
                            "bloom literal", "bare", "[", "{"
                            ],
    "<more-condition>" : ["moss", ";"],
    "<else>" : ";",
    "<iterative>" : ";",
    "<argument>" : ")",
    "<add-argument>" : ")",
    "<function>" : "plant",
    "<parameter>" : ")",
    "<add-parameter>" : ")"
    }

predict_set = {
    "FIRST(program)" : "seed",
    "FIRST(import)" : "transplant",
    "FOLLOW(import)" : ["floral", "garden"],
    "FIRST(global)" : "floral",
    "FOLLOW(global)" : "garden",
    "FIRST(statement->local-variable)" : [
                                        "tint", "flora", "chard",
                                        "string", "bloom", "florist",
                                        "tulip", "dirt", "stem"
                                        ],
    "FIRST(statement->i/o-statement)" : [
                                        "tint", "flora", "chard",
                                        "string", "bloom", "florist",
                                        "tulip", "dirt", "stem",
                                        "#", "inpetal", "mint"
                                        ],
    "FIRST(statement->assignment)" : ["tint literal", "flora literal", "#"],
    "FIRST(statement->leaf)" : "leaf",
    "FIRST(statement->iterative)" : ["fern", "willow"],
    "FIRST(statement->math)" : ["tint literal", "flora literal", "#", "(", "string literal"],
    "FIRST(statement->identifier)" : "#",
    "FIRST(statement->clear)" : "clear",
    "FIRST(<statement->break)" : "break",
    "FOLLOW(statement)" : [")", "regrow"],
    "FIRST(local-variable->tint)" : "tint",
    "FIRST(local-variable->flora)" : "flora",
    "FIRST(local-variable->chard)" : "chard",
    "FIRST(local-variable->string)" : "string",
    "FIRST(local-variable->bloom)" : "bloom",
    "FIRST(local-variable->florist)" : "florist",
    "FIRST(local-variable->tulip)" : "tulip",
    "FIRST(local-variable->dirt)" : "dirt",
    "FIRST(local-variable->stem)" : "stem",
    "FIRST(tint-value)" : "=",
    "FOLLOW(tint-value)" : [",", "$"],
    "FIRST(flora-value)" : "=",
    "FOLLOW(flora-value)" : [",", "$"],
    "FIRST(chard-value)" : "=",
    "FOLLOW(chard-value)" : [",", "$"],
    "FIRST(string-value)" : "=",
    "FOLLOW(string-value)" : [",", "$"],
    "FIRST(bloom-value)" : "=",
    "FOLLOW(bloom-value)" : [",", "$"],
    "FIRST(florist-value)" : "=",
    "FOLLOW(florist-value)" : [",", "$"],
    "FIRST(tulip-stem-value)" : "=",
    "FOLLOW(tulip-stem-value)" : [",", "$"],
    "FIRST(dirt-value)" : "=",
    "FOLLOW(dirt-value)" : [",", "$"],
    "FIRST(tint->tint literal)" : "tint literal",
    "FIRST(tint->identifier)" : "#",
    "FIRST(flora->flora literal)" : "flora literal",
    "FIRST(flora->identifier)" : "#",
    "FIRST(chard->chard literal)" : "chard literal",
    "FIRST(chard->identifier)" : "#",
    "FIRST(string->string literal)" : "string literal",
    "FIRST(string->identifier)" : "#",
    "FIRST(bloom->bloom literal)" : "bloom literal",
    "FIRST(bloom->identifier)" : "#",
    "FIRST(dirt->string literal)" : "string literal",
    "FIRST(dirt->identifier)" : "#",
    "FIRST(numeric->tint literal)" : "tint literal",
    "FIRST(numeric->flora literal)" : "flora literal",
    "FIRST(numeric->identifier)" : "#",
    "FIRST(all-value->numeric)" : ["tint literal", "flora literal", "#"],
    "FIRST(all-value->chard literal)" : "chard literal",
    "FIRST(all-value->string literal)" : "string literal",
    "FIRST(all-value->bloom literal)" : "bloom literal",
    "FIRST(all-value->bare)" : "bare",
    "FIRST(all-value->florist)" : "[",
    "FIRST(all-value->tulip-stem)" : "{",
    "FIRST(all-value->dirt)" : "{",
    "FIRST(more-value)" : ",",
    "FOLLOW(more-value)" : ["]", "}"],
    "FIRST(more-pair-value)" : ",",
    "FOLLOW(more-pair-value)" : "}",
    "FIRST(index)" : "[",
    "FOLLOW(index)" : [",", "]", "}", ")", ";", "=", "!", "["],
    "FIRST(dirt-key)" : "[",
    "FOLLOW(dirt-key)" : ["[", ",", "]", "}", ")", ";", "=", "!"],
    "FIRST(more-tint)" : ",",
    "FOLLOW(more-tint)" : [";", ",", "$"],
    "FIRST(more-flora)" : ",",
    "FOLLOW(more-flora)" : [";", ",", "$"],
    "FIRST(more-chard)" : ",",
    "FOLLOW(more-chard)" : [";", ",", "$"],
    "FIRST(more-string)" : ",",
    "FOLLOW(more-string)" : [";", ",", "$"],
    "FIRST(more-bloom)" : ",",
    "FOLLOW(more-bloom)" : [";", ",", "$"],
    "FIRST(more-florist)" : ",",
    "FOLLOW(more-florist)" : [";", ",", "$"],
    "FIRST(more-tulip-stem)" : ",",
    "FOLLOW(more-tulip-stem)" : [";", ",", "$"],
    "FIRST(more-dirt)" : ",",
    "FOLLOW(more-dirt)" : [";", ",", "$"],
    "FIRST(i/o-statement->inpetal)" : [
                                    "tint", "flora", "chard",
                                    "string", "bloom", "florist",
                                    "tulip", "dirt", "stem",
                                    "#", "inpetal"
                                    ],
    "FIRST(i/o-statement->mint)" : "mint",
    "FIRST(inpetal-receiver->datatype)" : ["tint", "flora", "chard", "string", "bloom"],
    "FIRST(inpetal-receiver->florist)" : "florist",
    "FIRST(inpetal-receiver->tulip)" : "tulip",
    "FIRST(inpetal-receiver->dirt)" : "dirt",
    "FIRST(inpetal-receiver->stem)" : "stem",
    "FIRST(inpetal-receiver->identifier)" : "#",
    "FOLLOW(inpetal-receiver)" : "inpetal",
    "FIRST(datatype->tint)" : "tint",
    "FIRST(datatype->flora)" : "flora",
    "FIRST(datatype->chard)" : "chard",
    "FIRST(datatype->string)" : "string",
    "FIRST(datatype->bloom)" : "bloom",
    "FIRST(mint-entry->all-value)" : [
                                    "tint literal", "flora literal",
                                    "#", "chard literal", "string literal",
                                    "bloom literal", "bare", "[", "{"
                                    ],
    "FIRST(mint-entry->math)" : ["tint literal", "flora literal", "#", "(", "string literal"],
    "FOLLOW(mint-entry)" : ")",
    "FIRST(math->numeric)" : ["tint literal", "flora literal", "#"],
    "FIRST(math->())" : "(",
    "FIRST(math->string)" : "string literal",
    "FIRST(start-operation->operator)" : ["+", "-", "*", "/", "%", "(", "$", ";", ")"],
    "FIRST(start-operation->())" : "(",
    "FOLLOW(start-operation)" : [";", ")"],
    "FIRST(operator->+)" : "+",
    "FIRST(operator->-)" : "-",
    "FIRST(operator->*)" : "*",
    "FIRST(operator->/)" : "/",
    "FIRST(operator->%)" : "%",
    "FIRST(operator->**)" : "*",
    "FIRST(operator->//)" : "/",
    "FOLLOW(operator)" : ["+", "-", "*", "/", "%", ";", ")", "(", "$"],
    "FIRST(concatenate)" : "+",
    "FOLLOW(concatenate)" : [";", ")"],
    "FIRST(assignment->numeric)" : ["tint literal", "flora literal", "#"],
    "FIRST(assignment->string)" : ["string literal", "#"],
    "FIRST(assignment->identifier)" : "#",
    "FIRST(assignment-op->equals-plus)" : ["=", "+"],
    "FIRST(assignment-op->-=)" : "-",
    "FIRST(assignment-op->*=)" : "*",
    "FIRST(assignment-op->/=)" : "/",
    "FIRST(assignment-op->%=)" : "%",
    "FIRST(assignment-op->**=)" : "*",
    "FIRST(assignment-op->//=)" : "/",
    "FIRST(equals-plus->=)" : "=",
    "FIRST(equals-plus->+=)" : "+",
    "FIRST(condition->numeric)" : ["tint literal", "flora literal", "#"],
    "FIRST(condition->all-value)" : [
                                    "tint literal", "flora literal", "#",
                                    "chard literal", "string literal",
                                    "bloom literal", "bare", "[", "{"
                                    ],
    "FIRST(numeric-condition)" : ["=", "!", ">", "<"],
    "FOLLOW(numeric-condition)" : ")",
    "FIRST(string-condition)" : ["=", "!"],
    "FOLLOW(string-condition)" : ")",
    "FIRST(numeric-cond-op->==)" : "=",
    "FIRST(numeric-cond-op->!=)" : "!",
    "FIRST(numeric-cond-op-> >)" : ">",
    "FIRST(numeric-cond-op-> <)" : "<",
    "FIRST(numeric-cond-op->>=)" : ">",
    "FIRST(numeric-cond-op-><=)" : "<",
    "FIRST(numeric-cond-op->=&)" : "=",
    "FIRST(numeric-cond-op->=/)" : "=", 
    "FIRST(string-cond-op->==)" : "=",
    "FIRST(string-cond-op->!=)" : "!",
    "FIRST(string-cond-op->=&)" : "=",
    "FIRST(string-cond-op->=/)" : "=",
    "FIRST(more-condition)" : "eleaf",
    "FOLLOW(more-condition)" : ["moss", ";"],
    "FIRST(else)" : "moss",
    "FOLLOW(else)" : ";",
    "FIRST(iterative->fern)" : "fern",
    "FIRST(iterative->willow)" : "willow",
    "FIRST(argument)" : [
                        "tint literal", "flora literal", "#",
                        "chard literal", "string literal",
                        "bloom literal", "bare", "[", "{"
                        ],
    "FOLLOW(argument)" : ")",
    "FIRST(add-argument)" : ",",
    "FOLLOW(add-argument)" : ")",
    "FIRST(function->datatype)" : ["tint", "flora", "chard", "string", "bloom"],
    "FIRST(function->viola)" : "viola",
    "FOLLOW(function)" : "plant",
    "FIRST(parameter)" : ["tint", "flora", "chard", "string", "bloom"],
    "FOLLOW(parameter)" : ")",
    "FIRST(add-parameter)" : ",",
    "FOLLOW(add-parameter)" : ")"
    }