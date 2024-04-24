function opcDesplegable(){
    var desplegable = document.getElementById('desplegable');
    var infoRellenar = document.getElementById('infoRellenar');
    var retrievedInfo = document.getElementById('retrievedInfo');
    var selectedOption = desplegable.value;
    var content = '';
    var retrievedContent = '';
    switch(selectedOption) {
        case 'cliente':
            content = `
            <div class="infoRellenar">
                <h1 style="margin-bottom: 20px;">Tabla Cliente</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>
                        <div class="elemento">
                            <label for="idCliente">ID</label><br>
                            <input type="text" id="idCliente" name="idCliente" required="true"/>
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
                <h1 style="margin-bottom: 20px;">Tabla Restaurante</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>
                        <div class="elemento">
                            <label for="nitRest">NIT</label><br>
                            <input type="text" id="nitRest" name="nitRest" required="true"/>
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
                <h1 style="margin-bottom: 20px;">Tabla Factura</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>
                        <div class="elemento">
                            <label for="idFact">ID Factura</label><br>
                            <input type="text" id="idFact" name="idFact" required="true"/>
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
                <h1 style="margin-bottom: 20px;">Tabla Detalles de Factura</h1>
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
                <h1 style="margin-bottom: 20px;">Tabla Producto</h1>
                <div class="selectedOpc" id=selectedOpc">
                    <form>                  
                        <div class="elemento">
                            <label for="codProd">Código Producto</label><br>
                            <input type="text" id="codProd" name="codProd" required="true"/>
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
                    <h1 style="margin-bottom: 20px;">Tabla Proveedor</h1>
                    <div class="selectedOpc" id=selectedOpc">
                        <form>                  
                            <div class="elemento">
                                <label for="nitProv">NIT Proveedor</label><br>
                                <input type="text" id="nitProv" name="nitProv" required="true"/>
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
            retrievedContent = '';
    }
    infoRellenar.innerHTML = content;
};

document.getElementById('desplegable').addEventListener('change', opcDesplegable);

function redirectIndex(){
    window.location.href = '../index.html'
}