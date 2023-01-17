from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from app.models import *
from app.forms import *
from datetime import datetime

def suma_importes(context, id):
    art_fac = Compra_linea_prov.objects.filter(compra_cliente_id = id)
    suma_importes = 0
    for i in art_fac:
        suma_importes += i.importe
    factura_last = Factura.objects.last()
    total_iva = suma_importes * (factura_last.iva/100) 
    total_fac = suma_importes + total_iva
    context['articulo_factura'] = art_fac
    context['suma_importe'] = suma_importes
    context['total_fac'] = total_fac


def define_context(context={},**kwargs):
    return {**context,**kwargs}

    
def orden_compra(request):

    compra_list = Compra_prov.objects.all()
    busquedaform = OrdenCompraBusqueda()
    context = { 
        'compra_list':compra_list,
        'busquedaform':busquedaform
    }
    if request.method == 'POST':
        busquedaform = OrdenCompraBusqueda(request.POST)
        if busquedaform.is_valid():
            data = Compra_prov.objects.all()
            data = data.filter(codprov__ruc=busquedaform.cleaned_data['rucproveedor'])  if busquedaform.cleaned_data['rucproveedor'] else data
            data = data.filter(factura_id=busquedaform.cleaned_data['numorden'])  if busquedaform.cleaned_data['numorden'] else data
            data = data.filter(factura__fecha=busquedaform.cleaned_data['fechaorden'])  if busquedaform.cleaned_data['fechaorden'] else data
            data = data.filter(recibido=busquedaform.cleaned_data['recibido'])  if busquedaform.cleaned_data['recibido'] else data
            context['compra_list']=data
            context['busquedaform']=busquedaform
    else:
        busquedaform = OrdenCompraBusqueda()

    return render(request, "CompraProv/compraprov_crud.html", context)

def agregar_orden_compra(request):


    context={
        'nueva_factura_form':NuevaFactura({'fecha': datetime.now(),'iva':18}),
        'nombre_factura':'Nueva operación de compra',
        'iva_factura':8
    }

    if request.method == 'POST':
        nueva_factura = NuevaFactura(request.POST)
        estado_registro = True if request.POST.get("estado_registro",False) == "True" else False
        cancelado = request.POST.get("cancelado", False)
        ruc_prov = request.POST.get('ruc_prov',None)
        reg_com_clie = request.POST.get('reg_com_clie',None)
        nombre_factura = request.POST.get('nombre_factura','')
        iva_factura = request.POST.get('iva_fac',None)
        mensaje_registro = request.POST.get('mensaje_registro','')
        valid_prov_form = request.POST.get("valid_prov_form",None)
        validfac_finalform = request.POST.get("validfac_finalform", None)

        eliminar_art_compra = request.POST.get("eliminar_art_compra",None)
        prov = Proveedores.objects.filter(ruc=ruc_prov)


        
        if ruc_prov!='' and nueva_factura.is_valid():
            nombre_prov = prov[0] if prov else "RUC INVÁLIDO"
            context = define_context(context,ruc_prov=ruc_prov,
                                    nombre_prov=nombre_prov,nueva_factura_form=nueva_factura)
        
        if not estado_registro and not cancelado:
            prov = Proveedores.objects.filter(ruc=ruc_prov)
            if ruc_prov!='':
                nombre_prov = prov[0] if prov else "RUC INVÁLIDO"
                context = define_context(context,ruc_prov=ruc_prov,
                                        nombre_prov=nombre_prov,nueva_factura_form=nueva_factura)
            
            if prov!=[] and reg_com_clie==ruc_prov:
                print(prov, 'prov1')
                print('estado de registro', estado_registro)
                nueva_factura.save()
                last_factura = Factura.objects.last()
                fac_prov = Compra_prov()
                fac_prov.codprov = prov[0]
                fac_prov.compra = last_factura
                fac_prov.save()
                compra_prov = Compra_prov.objects.last()
                context = define_context(context,
                                        mensaje_registro='succeed',
                                        nombre_factura='COMPRA N° '+str(last_factura.pk),
                                        estado_registro=True,
                                        iva_factura=last_factura.iva,
                                        compra_prov=compra_prov)

        else:
            if cancelado and ruc_prov:
                last = Factura.objects.filter(pk=int(nombre_factura[10:]))
                last[0].delete()
                return redirect("agcompra")


                '''
                realizar todas las operaciones siguientes
                los botones estarán desahabilitados hasta que cancele la compra eliminandola con el botón cancelar
                '''

            if eliminar_art_compra:
                del_flc = Compra_linea_prov.objects.filter(pk=request.POST['eliminar_art_compra'])
                del_flc.delete()
                suma_importes(context,Compra_prov.objects.last().pk )
    

            if valid_prov_form:
                nomarticulo = request.POST["nomarticulo"] 
                articulo_data = Articulos.objects.get(referencia=nomarticulo)
                last_factura = Factura.objects.last()

                compra_prov = Compra_prov.objects.last()

                compra_linea_prov = Compra_linea_prov()
                compra_linea_prov.compra_cliente = compra_prov
                compra_linea_prov.codproducto = Articulos.objects.get(referencia=nomarticulo)
                compra_linea_prov.precio = articulo_data.precio_compra
                cantidad = request.POST["cantidad_art"]
                compra_linea_prov.cantidad = cantidad
                compra_linea_prov.importe = (articulo_data.precio_compra * int(cantidad))
                compra_linea_prov.save()    
                suma_importes(context, Compra_prov.objects.last().pk)
                context = define_context(context,
                                        mensaje_registro='succeed',
                                        nombre_factura='COMPRA N° '+str(last_factura.pk),
                                        estado_registro=True,
                                        iva_factura=last_factura.iva,
                                        compra_prov=compra_prov)
                print("======== PROV2")
                print(prov)

            #Modifica Factura
            if validfac_finalform:
                print("======== PROV3")
                print(prov)
                compra_put = Factura.objects.last()
                compra_put.totalfactura = request.POST["total_fac"]
                compra_put.save()
                com_clie_last = Compra_prov.objects.last()
                art_com = Compra_linea_prov.objects.filter(compra_cliente_id = com_clie_last.compra.id)
                context['articulo_factura'] = art_com
                context = define_context(context,
                                        mensaje_registro='succeed',
                                        nombre_factura='COMPRA N° '+str(compra_put.pk),
                                        estado_registro=True,
                                        iva_factura=compra_put.iva,
                                        compra_prov=com_clie_last)

    return render(request, "CompraProv/agregar_fac_prov.html", context)

def ver_orden(request):
    return 

def editar_orden(request, id):
    orden_compra = Compra_prov.objects.get(compra_id = id)
    art_com = Compra_linea_prov.objects.filter(compra_cliente_id = id)   
    context={
        'ord':orden_compra,
        'articulo_factura':art_com
    }
        
    if request.method == 'POST':
        recibidoCheck = request.POST.get('recibidoCheck',None)
        descripciontext = request.POST.get('descripciontext',None)
        imgfactura = request.POST.get('imgfactura',None)
        compra_prov = Compra_prov()
        compra_prov.recibido = recibidoCheck
        compra_prov.detaller_entrega = descripciontext


    return render(request, "CompraProv/compra_editar.html", context)

def eliminar_orden(request, id):
    enviado = False

    del_orden_liena = Compra_linea_prov.objects.filter(compra_cliente_id=id)
    del_orden_compra = Compra_prov.objects.get(pk=id)
    del_factura = Factura.objects.get(id=id)
    
    red = request.POST.get('compraprov','/erp/compraprov/')

    if request.method =="POST":
        for i in del_orden_liena:
            i.delete()

        del_orden_compra.delete()
        del_factura.delete()
        return HttpResponseRedirect(red)

    context = {
        'enviado':enviado
    }
    return render(request, "CompraProv/del_compra.html", context)
