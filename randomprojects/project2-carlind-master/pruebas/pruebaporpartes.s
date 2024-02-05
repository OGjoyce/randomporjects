////////////////////////////////////////////////////////////////////////////////////
/////////////////////////CIENCIAS DE LA COMPUTACON III - 2017///////////////////////
////////////////////////////////UNIVERSIDAD GALILEO/////////////////////////////////
///////////////////////////////Proyecto-2 Ensamblador///////////////////////////////
////////////////////////////////////////////////////////////////////////////////////

.data
ADD_: .asciz "ADD"
SUBS_: .asciz "SUBS"
SUB_: .asciz "SUB"
ADDS_: .asciz "ADDS"
AND_: .asciz "AND"
ORR_: .asciz "ORR"
EOR_: .asciz "EOR"
ANDS_: .asciz "ANDS"
LSLV_: .asciz "LSLV"
LSRV_: .asciz "LSRV"
ASRV_: .asciz "ASRV"
RORV_: .asciz "RORV"
MOVN_: .asciz "MOVN"
MOV_: .asciz "MOV"
MOVK_: .asciz "MOVK"
CBZ_: .asciz "CBZ"
CBNZ_: .asciz "CBNZ"
PRINT_CHAR: .asciz "%c\n"
READ_MODE: .asciz "r"
WORD: .space 100
HOPE: .asciz "TENGO LA ESPERANZA DE QUE AQUI SALGA LO QUE ESPERO %s\n"
TO_CODE_MESSAGE: .asciz "Instrucciones a Codificar:\n..........................\n%s"
CODED_MESSAGE:  .asciz "\nInstrucciones Codificadas:\n.........................."
INSTRUCCION_: .asciz "0x%08x\n"
args_error_msg: .asciz "No se Ingreso el Numero Correcto de Parametros"
dot_data: .space 1000   //el area de data
dot_text: .space 4000 //el area de texto
file_buffer: .space 8000//el buffer que guardara el texto a codificar
.text
  .globl main


////////////////////////////////////////////////////////////////////////////
//////////////////////////START READ FILE///////////////////////////////////
///////ESTA SECCION NO SE DEBE CAMBIAR, PERO ES BUENO QUE LA ENTIENDAN//////
//////////////X0: el buffer donde guardaremos los caracteres////////////////
////////////////////X1: el archivo que vamos a abrir////////////////////////
////////////////////////////////////////////////////////////////////////////
read_file:    //x0 es el buffer, x1 es el archivo
   ADD SP, SP, #-32
   STR x30,[SP,#0]
   STR x19,[SP,#8]
   STR x20,[SP,#16]
   STR x21,[SP,#24]
   MOV x19, x0    //el buffer
   MOV x20, x1    //el archivo
read_file_loop:
   MOV x0, x20
   BL fgetc
   MOV x21,x0
   MOV x0,x20
   BL feof
   CMP x0,#0
   B.NE read_file_finish
   STR x21,[x19,#0]
   ADD x19,x19, #1
   B read_file_loop
read_file_finish:
   MOV x9,#0    //un \0 diciendo que se acabo el archivo
   STR x9,[x19,#0]
   LDR x21,[SP,#24]
   LDR x20,[SP,#16]
   LDR x19,[SP,#8]
   LDR x30,[SP,#0]
   ADD SP, SP, #32
   RET
/////////////////////////////////////////////////////////////////////////////
///////////////////////////END READ FILE/////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////



/////////////////////////////////////////////////////////////////////////////
////////////////////////////DISPLAY INSTRUCTIONS/////////////////////////////
////////NO DEBEN CAMBIAR ESTA SECCION, PERO ES BUENO QUE LA ENTIENDAN////////
//////////////////x0: dot_text, para desplegar las instrucciones/////////////
/////////////////////////////////////////////////////////////////////////////
display_instructions:
   ADD SP, SP, #-16
   STR x30,[SP,#0]
   STR x19,[SP,#8]
   MOV x19, x0
   LDR x0,=CODED_MESSAGE
   BL puts
display_loop:
   LDR x0,=INSTRUCCION_
   LDR w1,[x19,#0]
   ADD x19,x19,#4
   CMP w1,#0
   B.EQ finish_display
   BL printf
   B display_loop
finish_display:
   LDR x19,[SP,#8]
   LDR x30,[SP,#0]
   ADD SP, SP, #16
   RET
//////////////////////////////////////////////////////////////////////////////
/////////////////////////END DISPLAY INSTRUCTIONS/////////////////////////////
//////////////////////////////////////////////////////////////////////////////





get_next_word:
   SUB SP, SP, #16
   STR x30, [SP,#0]
   LDR x9,=WORD
get_next_word_loop:
   LDRB w0, [x19,#0]
   ADD x19, x19, #1
   CMP w0,' '
   B.EQ finish_get_next_word
   CMP w0,'\n'
   B.EQ finish_get_next_word
   CMP w0, #0
   B.EQ finish_get_next_word
   STRB w0,[x9,#0]
   ADD x9, x9,#1
   B get_next_word_loop
finish_get_next_word:
   MOV w10,#0
   STRB w10,[x9,#0]
   LDR x30, [SP,#0]
   ADD SP, SP, #16
   RET


get_register:
  SUB SP, SP,#16
  STR x30,[SP,#0]
  LDR x0,=WORD
get_register_loop:
  LDRB w9,[x0,#0]
  CMP w9,','
  ADD x0,x0,#1
  B.EQ get_register_loop_coma
  //CMP w9,'#'
  //ADD x0,x0,#1
  //B.EQ immediate
  CMP w9,#0
  B.EQ get_register_finish
  B get_register_loop
get_register_loop_coma:
  SUB x0,x0,#1
  MOV w11,#0
  STRB w11,[x0,#0]  //QUITE LA COMA
//immediate:
  //SUB x0,x0,#1
  //MOV w11,#0
  //STRB w11,[x0,#0] //  QUITE #?  
get_register_finish:
  LDR x0,=WORD
  ADD x0, x0, #1  //QUITE LA x
  BL atoi
  LDR x30,[SP,#0]
  ADD SP, SP, #16
  RET   



//////////////////////////////////////////////////////////////////////////////
///////////////////////////////encode/////////////////////////////////////////
/////////////////////x0: buffer con las instrucciones/////////////////////////
/////////////////////////////x1: area de texto////////////////////////////////
/////////////////////////////x2: area de data ////////////////////////////////
///////////////////ESTA ES LA FUNCION QUE DEBEN IMPLEMENTAR///////////////////
//////////////////////////////////////////////////////////////////////////////
encode:
   SUB SP, SP,#32
   STR x30,[SP,#0]
   STR x19,[SP,#8]
   STR x20,[SP,#16]
   STR x21,[SP,#24]
   MOV x19, x0    //buffer
   MOV x20, x1    //texto
   MOV x21, x2    //data

//immediate_op:
  //si tiene numeral en la posicion 10
//immediate:
  //si tiene Numeral en la posicion 5

opciones:

BL get_next_word

   LDR x0,=ADD_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   //B.EQ add_case 
   B.EQ addi_case

   LDR x0,=ADDS_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   //B.EQ adds_case 
   B.EQ addsi_case

   LDR x0,=SUB_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   //B.EQ sub_case 
   B.EQ subi_case

   LDR x0,=SUBS_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   //B.EQ subs_case 
   B.EQ subsi_case

   LDR x0,=AND_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ and_case 

   LDR x0,=ORR_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ orr_case 

   LDR x0,=EOR_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ eor_case 

   LDR x0,=ANDS_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ ands_case 

   LDR x0,=LSLV_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ lslv_case 

   LDR x0,=LSRV_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ lsrv_case 

   LDR x0,=ASRV_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ asrv_case 

   LDR x0,=RORV_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ rorv_case 

   LDR x0,=MOVN_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ movn_case 

   LDR x0,=MOV_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ mov_case    

   LDR x0,=MOVK_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ movk_case    

   LDR x0,=CBZ_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ cbz_case   

   LDR x0,=CBNZ_
   LDR x1,=WORD
   BL strcmp
   CMP x0,#0
   B.EQ cbnz_case   

   B finish_encode

add_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0x8B0
   LSL w23, w23, #20

   B codificacion_r

adds_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xAB0
   LSL w23, w23, #20

   B codificacion_r

sub_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xCB0
   LSL w23, w23, #20

   B codificacion_r

subs_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xEB0
   LSL w23, w23, #20
   B codificacion_r  

and_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0x8A0
   LSL w23, w23, #20
   B codificacion_r

orr_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xAA0
   LSL w23, w23, #20

   B codificacion_r

   eor_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xCA0
   LSL w23, w23, #20

   B codificacion_r

ands_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xEA0
   LSL w23, w23, #20

   B codificacion_r

lslv_case:            //EN LOS SIGUIENTES 4 HACER COMPARACION CON EL OPCODE
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0x9AC
   LSL w23, w23, #20
   //MOV w24,#0x20
   //LSL w24, w24, #9
   B codificacion_r

lsrv_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0x9AC
   LSL w23, w23, #20
   //MOV w24,#0x24
   //LSL w24, w24, #9
   B codificacion_r

asrv_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0x9AC
   LSL w23, w23, #20
   //MOV w24,#0x28
   //LSL w24, w24, #9

   B codificacion_r

rorv_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0x9AC
   LSL w23, w23, #20
   //MOV w24,#0x2C
   //LSL w24, w24, #9


   B codificacion_r

   //TIPO I

addi_case:
   SUB SP, SP, #16
   STR x23, [SP,#0]
   MOV w23,#0x910
   LSL w23, w23, #20
   B codificacion_i 

addsi_case:
   SUB SP, SP, #16
   STR x23, [SP,#0]
   MOV w23,#0xB10
   LSL w23, w23, #20
   B codificacion_i  

subi_case:
   SUB SP, SP, #16
   STR x23, [SP,#0]
   MOV w23,#0xD10
   LSL w23, w23, #20
   B codificacion_i 

subsi_case:
   SUB SP, SP, #16
   STR x23, [SP,#0]
   MOV w23,#0xF10
   LSL w23, w23, #20
   B codificacion_i         

movn_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0x928
   LSL w23, w23, #20

   B codificacion_i

mov_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xD28
   LSL w23, w23, #20

   B codificacion_i

movk_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xF28
   LSL w23, w23, #20

   B codificacion_i

cbz_case:    //como funcionan los cbz?
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xB4
   LSL w23, w23, #23

   B codificacion_i

cbnz_case:
   SUB SP, SP, #16
   STR x23,[SP,#0]
   MOV w23,#0xB5
   LSL w23, w23, #23
   B codificacion_i

codificacion_r:

   BL get_next_word
   BL get_register
   ORR x23, x23, x0
   BL get_next_word
   BL get_register
   LSL x0, x0, #5
   ORR x23, x23, x0
   BL get_next_word
   BL get_register
   LSL x0, x0, #16
   ORR x23, x23, x0
   STR w23,[x20,#0]
   ADD x20, x20, #4
   LDR x23,[SP,#0]
   ADD SP, SP, #16
   
   B opciones

codificacion_i:
   
   BL get_next_word
   BL get_register
   ORR x23, x23, x0
   BL get_next_word
   BL get_register
   LSL x0, x0, #5
   ORR x23, x23, x0
   BL get_next_word
   BL get_register
   LSL x0, x0, #10
   ORR x23, x23, x0
   STR w23,[x20,#0]
   ADD x20, x20, #4
   LDR x23,[SP,#0]
   ADD SP, SP, #16

   B opciones   
  

finish_encode:
   LDR x21,[SP,#24]
   LDR x20,[SP,#16]
   LDR x19,[SP,#8]
   LDR x30,[SP,#0]
   ADD SP, SP, #32
   RET
//////////////////////////////////////////////////////////////////////////////
//////////////////////////////FINISH ENCODE///////////////////////////////////
//////////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////MAIN////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////
main:
   ADD SP, SP, #-16
   STR x30,[SP,#0]
   CMP x0, #2
   BNE args_error
   MOV x27, x1    //argv se guarda en x27
   LDR x19,=file_buffer //x19 guarda el buffer de caracteres ya leidos
   LDR x20,=dot_text  //x20 guarda el area de texto
   LDR x21,=dot_data  //x21 guarda el area de data
   LDR x0,[x27,#8]
   LDR x1,=READ_MODE
   BL fopen
   MOV x22, x0    //el archivo del que leeremos esta en x22
   MOV x0, x19
   MOV x1, x22
   BL read_file   //leemos el archivo completo
   MOV x0, x22
   BL fclose
   LDR x0,=TO_CODE_MESSAGE
   MOV x1,x19
   BL printf    //vamos a imprimir que hay en el buffer
   MOV x0, x19    //x0 tendra el buffer
   MOV x1, x20    //x1 tendra el area de texto
   MOV x2, x21    //x2 tendra el area de data
   BL encode    //esta es la ultima instruccion que hay que codificar
   MOV x0, x20      //desplegaremos las instrucciones codificadas
   BL display_instructions
main_finish:
   MOV x0,#0    // return 0 :)
   LDR x30,[SP,#0]
   ADD SP, SP, #16
   RET
args_error:
   LDR x0,=args_error_msg
   BL puts
   B main_finish