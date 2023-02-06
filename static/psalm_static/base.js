
$(document).ready(function(){
$(".hidden-textbox").hide();
$("select#form_interprise").change(function(){
var currentVal = $(this).val();
if(currentVal == "others"){
$(".hidden-textbox").show();
}
else
$(".hidden-textbox").hide();
});  
});


$(document).ready(function(){
$(".hidden-textbox2").hide();
$("select#industry_cluster").change(function(){
var currentVal = $(this).val();
if(currentVal == ""){
$(".hidden-textbox2").show();
}
else
$(".hidden-textbox2").hide();
});  
});

$(document).ready(function(){
$(".hidden-column_18_21").hide();
$("select#type_assistance").change(function(){
var currentVal = $(this).val();
if(currentVal == "product_dev"){
$(".hidden-column_18_21").show();
}
else
$(".hidden-column_18_21").hide();
});  
});


$(document).ready(function(){
$(".hidden-column_9_18").hide();
$("select#type_inv_match").change(function(){
var currentVal = $(this).val();
if(currentVal == "expansion" || currentVal == "productive_investment"){
$(".hidden-column_9_18").show();
}
else
$(".hidden-column_9_18").hide();
});  
});

$(document).ready(function(){
$(".hidden-column_19_26").hide();
$("select#type_inv_match").change(function(){
var currentVal = $(this).val();
if(currentVal == "rehabilitation"){
$(".hidden-column_19_26").show();
}
else
$(".hidden-column_19_26").hide();
});  
});

$(document).ready(function(){
$(".hidden-column_22_28").hide();
$("select#type_assistance").change(function(){
var currentVal = $(this).val();
if(currentVal == "consultancy_serv"){
$(".hidden-column_22_28").show();
}
else
$(".hidden-column_22_28").hide();
});  
});



$(document).ready(function(){
$(".hidden-textbox3").hide();
$("select#no_indigenous_group").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox3").show();
}
else
$(".hidden-textbox3").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox4").hide();
$("select#form_interprise2").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox4").show();
}
else
$(".hidden-textbox4").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox5").hide();
$("select#pricing").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox5").show();
}
else
$(".hidden-textbox5").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox6").hide();
$("select#quality_raw").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox6").show();
}
else
$(".hidden-textbox6").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox7").hide();
$("select#quality_final_prod").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox7").show();
}
else
$(".hidden-textbox7").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox8").hide();
$("select#existing_comm").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox8").show();
}
else
$(".hidden-textbox8").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox9").hide();
$("select#prov_supp_assis").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox9").show();
}
else
$(".hidden-textbox9").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox10").hide();
$("select#business_prodc3").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox10").show();
}
else
$(".hidden-textbox10").hide();
});  
});
$(document).ready(function(){
$(".hidden-textbox11").hide();
$("select#member_following").change(function(){
var currentVal = $(this).val();
if(currentVal == "orgs"){
$(".hidden-textbox11").show();
}
else
$(".hidden-textbox11").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox12").hide();
$("select#member_livelihood").change(function(){
var currentVal = $(this).val();
if(currentVal == "Yes"){
$(".hidden-textbox12").show();
}
else
$(".hidden-textbox12").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox13").hide();
$("select#dip_alignment_prod").change(function(){
var currentVal = $(this).val();
if(currentVal == "dipyesprod"){
$(".hidden-textbox13").show();
}
else
$(".hidden-textbox13").hide();
});  
});


$(document).ready(function(){
$(".hidden-textbox14").hide();
$("select#dip_alignment").change(function(){
var currentVal = $(this).val();
if(currentVal == "dipyes"){
$(".hidden-textbox14").show();
}
else
$(".hidden-textbox14").hide();
});  
});

$(document).ready(function(){
$(".hidden-textbox15").hide();
$("select#title_cert").change(function(){
var currentVal = $(this).val();
if(currentVal == "other_specifics"){
$(".hidden-textbox15").show();
}
else
$(".hidden-textbox15").hide();
});  
});

$(document).ready(function(){
    $(".hidden-textbox17").hide();
    $("select#training_act_en").change(function(){
    var currentVal = $(this).val();
    if(currentVal == "training_act_spec"){
    $(".hidden-textbox17").show();
    }
    else
    $(".hidden-textbox17").hide();
    });  
    });

 
$(document).ready(function(){
$(".hidden-textbox16").hide();
$("select#title_cert2").change(function(){
var currentVal = $(this).val();
if(currentVal == "others_specifics"){
$(".hidden-textbox16").show();
}
else
$(".hidden-textbox16").hide();
});  
});


$(document).ready(function(){
    $(".hidden-textbox19").hide();
    $("select#industry_clus_eq").change(function(){
    var currentVal = $(this).val();
    if(currentVal == "specsss"){
    $(".hidden-textbox19").show();
    }
    else
    $(".hidden-textbox19").hide();
    });  
    });

    window.onload = function(){
      document.getElementById('viewgraph').click();
      document.getElementById('viewchart').click();
    }

   


function myFunction() {
var checkbox1 = document.getElementById("business_reg_check");
var checkbox2 = document.getElementById("product_reg_check");
var checkbox3 = document.getElementById("cert_reg");
var checkbox4 = document.getElementById("lic_op");
var checkbox5 = document.getElementById("iso_cert");
var checkbox6 = document.getElementById("gapgmp_cert");
var checkbox7 = document.getElementById("organic");
var checkbox8 = document.getElementById("halal");
var checkbox9 = document.getElementById("other_cert");
var checkbox10 = document.getElementById("others_specific_products_checkbox");
var textt = document.getElementById("textt");
var textt2 = document.getElementById("textt2");
var textt3 = document.getElementById("textt3");
var textt4 = document.getElementById("textt4");
var textt5= document.getElementById("textt5");
var textt6 = document.getElementById("textt6");
var textt7 = document.getElementById("textt7");
var textt8 = document.getElementById("textt8");
var textt9 = document.getElementById("textt9");
var textt10 = document.getElementById("textt10");

if (checkbox1.checked == true){
textt.style.display = "block";
} else{
textt.style.display = "none";
}
if (checkbox2.checked == true){
textt2.style.display = "block";
} else {
textt2.style.display = "none";
}

if (checkbox3.checked == true){
textt3.style.display = "block";
} else {
textt3.style.display = "none";
}

if (checkbox4.checked == true){
textt4.style.display = "block";
} else {
textt4.style.display = "none";
}

if (checkbox5.checked == true){
textt5.style.display = "block";
} else{
textt5.style.display = "none";
}

if (checkbox5.checked == true){
iso_cert_specific.style.display = "block";
} else{
iso_cert_specific.style.display = "none";
}

if (checkbox6.checked == true){
textt6.style.display = "block";
} else {
textt6.style.display = "none";
}

if (checkbox6.checked == true){
textt6.style.display = "block";
} else {
textt6.style.display = "none";
}

if (checkbox7.checked == true){
textt7.style.display = "block";
} else {
textt7.style.display = "none";
}

if (checkbox8.checked == true){
textt8.style.display = "block";
} else {
textt8.style.display = "none";
}

if (checkbox9.checked == true){
textt9.style.display = "block";
} else {
textt9.style.display = "none";
}
if (checkbox9.checked == true){
other_cert_specify.style.display = "block";
} else {
other_cert_specify.style.display = "none";
}

if (checkbox10.checked == true){
others_specific_products.style.display = "block";
} else{
others_specific_products.style.display = "none";
}







}
function myFunction2() {

var checkbox11 = document.getElementById("other_orgs_checkbox");

if (checkbox11.checked == true){
    other_orgs_pls_spec.style.display = "block";
} else{
        other_orgs_pls_spec.style.display = "none";
}

}

function myFunction3() {

    var checkbox12 = document.getElementById("other_orgs_checkbox");
    
    if (checkbox12.checked == true){
        other_orgs_pls_spec.style.display = "block";
    } else{
            other_orgs_pls_spec.style.display = "none";
    }
    
    }

    $(function() {
        $('.sweetalerts').click(function(e) {
            e.preventDefault();
            
            Swal.fire({
                title: 'Do you want to save the changes?',
                showDenyButton: true,
                showCancelButton: true,
                confirmButtonText: 'Save',
                denyButtonText: `Don't save`,
              }).then((result) => {
                if (result.isConfirmed) {
                  document.getElementById('saveupdate').click();
                  
                } else if (result.isDenied) {
                  Swal.fire('Changes are not saved', '', 'info')
                }
              })
        });
        
    });


    
    



