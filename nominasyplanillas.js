// use la base de datos:
use('nominasyplanillas');

// insertar datos
db.familiar.insert([{
    "nombre_primero":"Juan",
    "nombre_segundo":"Carlos",
    "apellido_primero":"Martinez",
    "apellido_segundo":"Machan",
    "telefono1":"12345678",
    "telefono2":"12345678",
    "parentesco":"esposo",
    "empleado_id":ObjectId()}]);

db.puesto.insert([{
    "nombre":"Recursos humanos",
    "sueldo":2500,
    "horas":8,
    "bonos":1,
    "precio":1,
    "factor_hora_extra":1.5}]);

db.empleado.insert([{
    "nombre_primero":"Mariana",
    "nombre_segundo":"Mellisa",
    "apellido_primero":"Vega",
    "apellido_segundo":"Paredes",
    "fecha_nacimiento": Date(),
    "telefono1":"1234567",
    "telefono2":"1234567",
    "dpi":"1234567890",
    "nit":"1234567",
    "carnet_igss": "2345678",
    "jornada": "matutina",
    "estado": "casado",
    "puesto_id": ObjectId()}]);

db.bono.insert([{
    "nombre":"Productividad",
    "cantidad":2000,
    "porcentaje":2,
    "fecha_aplicacion":Date(),
    "empleado_id": ObjectId()}]);

db.descuento.insert([{
    "nombre":"Igss",
    "porcentaje":4,
    "fecha_aplicacion":Date(),
    "cantidad": 240,
    "empleado_id": ObjectId()}]);

db.hora_extra.insert([{
    "cantidad":1,
    "fecha": Date(),
    "valor_calculo":400,
    "planilla_id": ObjectId()}]);

db.planilla.insert([{
    "numero_de_pago":1,
    "numero_de_planilla":1,
    "numero_de_documento_de_pago":1,
    "monto_ordinario": 3000,
    "dia_pago": 1,
    "empleado_id": ObjectId()
}]);
db.detalle_planilla.insert([{
    "sueldo_extraordinario":1,
    "bonificaciones":1,
    "otros": 1,
    "total_devengado": 0,
    "total_de_descuento": 3000,
    "total_liquido": 1,
    "igss": 1,
    "isr": 1,
    "judicial": "nacional",
    "anticipo": 0,
    "planilla_id": ObjectId(),
    "comisiones": 1
}]);
