var row=-1;
var uiu=[];

/**
 * Deletes a uiuTable row
 * @method delRow
 * @param {} id row number
 * @return
 */
function delRow(id){
    $('#ti-'+id).remove();
    numRows();
    for (var i=0; i<uiu.length; i++)
    {
        if (uiu[i].id === id)
            {
                uiu.splice(i,1);
                break;
            }
        }
}


/**
 * Counts uiuTable rows
 * @method numRows
 * @return
 */
function numRows(){
    $('#uiuTable tr').each(function(index){
        $(this).children("td:first").html(index);
    });
}


/**
 * Adds uiu row to uiuTable
 * @method addUiu
 * @return
 */
function addUiu(){
    var fg=$("#uiuForm input[name=modal_uiu_foglio]").val();
    var num=$("#uiuForm input[name=modal_uiu_numero]").val();
    var obj={'fg':fg, 'num':num};
    if (fg!=='' && num!=='')
    {
        var found=false;
        for (var i=0; i<uiu.length; i++)
        {
            if (uiu[i].fg === obj.fg && uiu[i].num === obj.num)
            {
                found=true;
                break;
            }
        }
        if (!found)
        {
            numRows();
            var rows = $('#uiuTable tr').length;
            $('#uiuTable tr:last').after('<tr id="ti-'+rows+'"><td>'+rows+'</td><td><span class="icon-trash" onClick="delRow('+rows+');"></span></td><td>'+fg+'</td><td>'+num+'</td></tr>');
            obj.id=rows;
            uiu.push(obj);
        }
    }
}


/**
 * Clear form and uiuTable rows
 * @method clearForm
 * @return
 */
function clearForm(){
    $('#cduForm')[0].reset();
    $( "#uiuTable tr:gt(0)").remove();
    uiu=[];
}


 /**
  * Adds uiu array values to the cduForm
  * @method submitHandler
  * @return
  */
 function appendUiu()
 {
     for (var i=0; i<uiu.length;i++)
     {
         $('#cduForm').append('<input type="hidden" name="uiu-'+i+'" value="'+
                              uiu[i].fg+'-'+uiu[i].num+'" />');
     }
 }


/**
 * Checks if uiu array contains elements
 * @method checkUiu
 * @return Boolean
 */
function checkUiu(){
  if (uiu.length === 0)
     return false;
  else
     return true;
}

/**
 * Checks if at least an urbanistic plan is selected
 * @method checkPlans
 * @return Boolean
 */
function checkPlans(){
    if ($('form input:checkbox:checked').length > 0)
        return true;
    else
        return false;
}
