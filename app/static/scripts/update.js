function opcDesplegable(){
    var desplegable = document.getElementById('desplegable');
    var infoRellenar = document.getElementById('infoRellenar');
    var selectedOption = desplegable.value;
    var content = '';
    switch(selectedOption) {
        case 'cliente':
            content = `
            <div class="infoRellenar">
                <h1 style="margin-bottom: 20px;">Información Cliente</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>
                        <div class="elemento">
                            <label for="idCliente">ID</label><br>
                            <input type="text" id="idCliente" name="idCliente" required="true"/>
                        </div>
                        <div class="elemento">
                            <label for="NomCliente">Nombre</label><br>
                            <input type="text" id="NomCliente" name="NomCliente">
                        </div>
                        <div class="elemento">
                            <label for="mailCliente">Email</label><br>
                            <input type="email" id="mailCliente" name="mailCliente"/>
                        </div>
                        <div class="elemento">
                            <label for="telCliente">Teléfono</label><br>
                            <input type="text" id="Telefono" name="Telefono">
                        </div>
                        <div class="elemento">
                            <input type="submit" value="Enviar"/>
                            <input type="button" value="Regresar" onclick="redirectIndex()"/>
                        </div>
                    </form>
                </div>
            </div>
            `;
            break;
        case 'restaurante':
            content = `
            <div class="infoRellenar">
                <h1 style="margin-bottom: 20px;">Información Restaurante</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>
                        <div class="elemento">
                            <label for="nitRest">NIT</label><br>
                            <input type="text" id="nitRest" name="nitRest" required="true"/>
                        </div>
                        <div class="elemento">
                            <label for="NomRest">Nombre</label><br>
                            <input type="text" id="NomRest" name="NomRest">
                        </div>
                        <div class="elemento">
                            <label for="Apertura">Hora Apertura</label><br>
                            <input type="time" id="Apertura" name="Apertura"/>
                        </div>
                        <div class="elemento">
                            <label for="Cerrado">Hora Cerrado</label><br>
                            <input type="time" id="Cerrado" name="Cerrado"/>
                        </div>
                        <div class="elemento">
                            <label for="UbiRest">Ubicación</label><br>
                            <input type="text" id="ubi" name="ubi"/>
                        </div>
                        <div class="elemento">
                            <input type="submit" value="Enviar"/>
                            <input type="button" value="Regresar" onclick="redirectIndex()"/>
                        </div>
                    </form>
                </div>
            </div>
            `;
            break;
        case 'factura':
            content = `
            <div class="infoRellenar">
                <h1 style="margin-bottom: 20px;">Información Factura</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>
                    <div class="elemento">
                        <label for="idFactura">ID Factura</label><br>
                        <input type="text" id="idFactura" name="idFactura" required="true"/>
                    </div>
                        <div class="elemento">
                            <label for="nitRest">NIT Restaurante</label><br>
                            <input type="text" id="nitRest" name="nitRest"/>
                        </div>
                        <div class="elemento">
                            <label for="idCliente">ID Cliente</label><br>
                            <input type="text" id="idCliente" name="idCliente"/>
                        </div>
                        <div class="elemento">
                            <label for="totalValor">Total Valor</label><br>
                            <input type="text" id="totalValor" name="totalValor"/>
                        </div>
                        <div class="elemento">
                            <label for="medioPago">Medio de Pago</label><br>
                            <input type="text" id="medioPago" name="medioPago"/>
                        </div>
                        <div class="elemento">
                            <label for="totalProductos">Total Productos</label><br>
                            <input type="text" id="totalProductos" name="totalProductos"/>
                        </div>
                        <div class="elemento">
                            <label for="FyH">Fecha y Hora</label><br>
                            <input type="datetime-local" id="FyH" name="FyH"/>
                        </div>
                        <div class="elemento">
                            <input type="submit" value="Enviar"/>
                            <input type="button" value="Regresar" onclick="redirectIndex()"/>
                        </div>
                    </form>
                </div>
            </div>
            `;
            break;
        case 'DF':
            content = `
            <div class="infoRellenar">
                <h1 style="margin-bottom: 20px;">Detalle Factura</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>
                        <div class="elemento">
                            <label for="idFactura">ID Factura</label><br>
                            <input type="text" id="idFactura" name="idFactura" required="true"/>
                        </div>
                        <div class="elemento">
                            <label for="codProd">Código Producto</label><br>
                            <input type="text" id="codProd" name="codProd" required="true"/>
                        </div>               
                        <div class="elemento">
                            <label for="nitRest">NIT Restaurante</label><br>
                            <input type="text" id="nitRest" name="nitRest"/>
                        </div>
                        <div class="elemento">
                            <label for="cant">Cantidad Comprada</label><br>
                            <input type="number" id="cant" name="cant"/>
                        </div>
                        <div class="elemento">
                            <input type="submit" value="Enviar"/>
                            <input type="button" value="Regresar" onclick="redirectIndex()"/>
                        </div>
                    </form>
                </div>
            </div>
            `;
            break;
        case 'producto':
            content = `
            <div class="infoRellenar">
                <h1 style="margin-bottom: 20px;">Información Producto</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>         
                        <div class="elemento">
                            <label for="codProd">Código Producto</label><br>
                            <input type="text" id="nitProv" name="nitProv" required="true"/>
                        </div>         
                        <div class="elemento">
                            <label for="nitProv">NIT Proveedor</label><br>
                            <input type="text" id="nitProv" name="nitProv"/>
                        </div>
                        <div class="elemento">
                            <label for="nomProd">Nombre Producto</label><br>
                            <input type="text" id="nomProd" name="nomProd"/>
                        </div>
                        <div class="elemento">
                            <label for="precioProd">Precio Producto</label><br>
                            <input type="number" id="precioProd" name="precioProd"/>
                        </div>
                        <div class="elemento">
                            <label for="catProd">Categoría Producto</label><br>
                            <input type="text" id="catProd" name="catProd"/>
                        </div>
                        <div class="elemento">
                            <input type="submit" value="Enviar"/>
                            <input type="button" value="Regresar" onclick="redirectIndex()"/>
                        </div>
                    </form>
                </div>
            </div>
            `;
            break;
            case 'proveedor':
                content = `
                <div class="infoRellenar">
                    <h1 style="margin-bottom: 20px;">Información Proveedor</h1>
                    <div class="selectedOpc" id=selectedOpc">
                        <form>                  
                            <div class="elemento">
                                <label for="nitProv">NIT Proveedor</label><br>
                                <input type="text" id="nitProv" name="nitProv" required="true"/>
                            </div>
                            <div class="elemento">
                                <label for="ubiProveedor">Ubicación Proveedor</label><br>
                                <input type="text" id="ubiProveedor" name="ubiProveedor"/>
                            </div>
                            <div class="elemento">
                                <label for="telProveedor">Teléfono Proveedor</label><br>
                                <input type="text" id="telProveedor" name="telProveedor"/>
                            </div>
                            <div class="elemento">
                                <input type="submit" value="Enviar"/>
                                <input type="button" value="Regresar" onclick="redirectIndex()"/>
                            </div>
                        </form>
                    </div>
                </div>
                `;
                break;
            case 'inventario':
                content = `
                <div class="infoRellenar">
                    <h1 style="margin-bottom: 20px;">Inventario</h1>
                    <div class="selectedOpc" id=selectedOpc">
                        <form>                  
                            <div class="elemento">
                                <label for="nitProv">NIT Proveedor</label><br>
                                <input type="text" id="nitProv" name="nitProv" required="true"/>
                            </div>
                            <div class="elemento">
                                <label for="nitRest">NIT Restaurante</label><br>
                                <input type="text" id="nitRest" name="nitRest" required="true"/>
                            </div>
                            <div class="elemento">
                                <label for="cantProducto">Cantidad Producto</label><br>
                                <input type="text" id="cantProducto" name="cantProducto"/>
                            </div>
                            <div class="elemento">
                                <input type="submit" value="Enviar"/>
                                <input type="button" value="Regresar" onclick="redirectIndex()"/>
                            </div>
                        </form>
                    </div>
                </div>
                `;
                break;
        default:
            content = '';
    }
    infoRellenar.innerHTML = content;
};

document.getElementById('desplegable').addEventListener('change', opcDesplegable);

function redirectIndex(){
    window.location.href = '../index.html'
}