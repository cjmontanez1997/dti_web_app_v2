from flask import Flask, Blueprint,request, flash, render_template, url_for,redirect, session
from modules.Connections import mysql
from decimal import Decimal
from flask_session import Session
import Configurations as c

db = mysql(*c.DB_CRED)
db.err_page = 0
app = Blueprint("form_c",__name__,template_folder="pages")

def is_on_session(): return ('USER_DATA' in session)

@app.route('/formc')
def index():
    return render_template("index.html")

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        position_firm = request.form['position_firm']
        member_indegenous = request.form['member_indegenous']
        sex = request.form.get('sex')
        age = request.form['age']
        contact_details = request.form['contact_details']
        email_add = request.form['email_add']
        vc_stakeholders = request.form.get('vc_stakeholders')
        industry_cluster = request.form.get('industry_cluster')
        pfn_specify = request.form['pfn_specify']
        reg_businessname = request.form['reg_businessname']
        business_addr = request.form['business_addr']
        form_interprise = request.form.get('form_interprise')
        interprise_other = request.form.get('interprise_other')
        issued_by_business_reg = request.form.get('issued_by_business_reg')
        expired_date_business_reg = request.form.get('expired_date_business_reg')
        issued_by_product_reg = request.form.get('issued_by_product_reg')
        expired_date_product_reg = request.form.get('expired_date_product_reg')
        issued_by_cert_reg = request.form.get('issued_by_cert_reg')
        expired_date_cert_reg = request.form.get('expired_date_cert_reg')
        issued_by_lic_op = request.form.get('issued_by_lic_op')
        expired_date_lic_op = request.form.get('expired_date_lic_op')
        iso_cert_specific = request.form.get('iso_cert_specific')
        issued_by_iso_cert = request.form.get('issued_by_iso_cert')
        expired_date_iso_cert = request.form.get('expired_date_iso_cert')
        issued_by_gapgmp_cert = request.form.get('issued_by_gapgmp_cert')
        expired_date_gapgmp_cert = request.form.get('expired_date_gapgmp_cert')
        issued_by_organic = request.form.get('issued_by_organic')
        expired_date_organic = request.form.get('expired_date_organic')
        issued_by_halal = request.form.get('issued_by_halal')
        expired_date_halal = request.form.get('expired_date_halal')
        other_cert_specify = request.form.get('other_cert_specify')
        issued_by_other_cert = request.form.get('issued_by_other_cert')
        expired_date_other_cert = request.form.get('expired_date_other_cert')
        none_of_the_above = request.form.get('none_of_the_above')
        type_enterprise = request.form.get('type_enterprise')
        store_capacity_organic = request.form.get('store_capacity_organic')
        store_capacity_synthetic = request.form.get('store_capacity_synthetic')
        potential_organic = request.form.get('potential_organic')
        potential_synthetic = request.form.get('potential_synthetic')
        other_info_organic = request.form.get('other_info_organic')
        other_info_synthetic = request.form.get('other_info_synthetic')
        store_capacity_pesticides = request.form.get('store_capacity_pesticides')
        store_capacity_herbicides = request.form.get('store_capacity_herbicides')
        potential_pesticides = request.form.get('potential_pesticides')
        potential_herbicides = request.form.get('potential_herbicides')
        other_info_pesticides = request.form.get('other_info_pesticides')
        other_info_herbicides = request.form.get('other_info_herbicides')
        store_capacity_vermicast_compost = request.form.get('store_capacity_vermicast_compost')
        potential_vermicast_compost = request.form.get('potential_vermicast_compost')
        other_info_vermicast_compost = request.form.get('other_info_vermicast_compost')
        store_capacity_seedlings = request.form.get('store_capacity_seedlings')
        potential_seedlings = request.form.get('potential_seedlings')
        other_info_seedlings = request.form.get('other_info_seedlings')
        others_specific_products = request.form.get('others_specific_products')
        store_capacity_others_specific_products = request.form.get('store_capacity_others_specific_products')
        potential_others_specific_products = request.form.get('potential_others_specific_products')
        other_info_others_specific_products = request.form.get('other_info_others_specific_products')
        area_capacity_drying = request.form.get('area_capacity_drying')
        potential_exp_drying = request.form.get('potential_exp_drying')
        other_info_drying = request.form.get('other_info_drying')
        area_capacity_storage_hauling = request.form.get('area_capacity_storage_hauling')
        potential_exp_storage_hauling = request.form.get('potential_exp_storage_hauling')
        other_info_storage_hauling = request.form.get('other_info_storage_hauling')
        current_capacity_semi_processing = request.form.get('current_capacity_semi_processing')
        potential_exp_semi_processing = request.form.get('potential_exp_semi_processing')
        other_info_semi_processing = request.form.get('other_info_semi_processing')
        current_capacity_final_product = request.form.get('current_capacity_final_product')
        potential_exp_final_product = request.form.get('potential_exp_final_product')
        other_info_final_product = request.form.get('other_info_final_product')
        volume_consolidation = request.form.get('volume_consolidation')
        potential_consolidation = request.form.get('potential_consolidation')
        other_info_consolidation = request.form.get('other_info_consolidation')
        production_pack_label = request.form.get('production_pack_label')
        potential_pack_label = request.form.get('potential_pack_label')
        other_info_pack_label = request.form.get('other_info_pack_label')
        loan_portfo_micro_financing = request.form.get('loan_portfo_micro_financing')
        potential_micro_financing = request.form.get('potential_micro_financing')
        other_info_micro_financing = request.form.get('other_info_micro_financing')
        loan_portfo_insurance = request.form.get('loan_portfo_insurance')
        potential_insurance = request.form.get('potential_insurance')
        other_info_insurance = request.form.get('other_info_insurance')
        prodsales_product_service = request.form.get('prodsales_product_service')
        prodsales_sales_vol = request.form.get('prodsales_sales_vol')
        prodsales_unit_selling = request.form.get('prodsales_unit_selling')
        prodsales_unit_measurement = request.form.get('prodsales_unit_measurement')
        prodsales_payment_terms = request.form.get('prodsales_payment_terms')
        prodsales_product_service2 = request.form.get('prodsales_product_service2')
        prodsales_sales_vol2 = request.form.get('prodsales_sales_vol2')
        prodsales_unit_selling2 = request.form.get('prodsales_unit_selling2')
        prodsales_unit_measurement2 = request.form.get('prodsales_unit_measurement2')
        prodsales_payment_terms2 = request.form.get('prodsales_payment_terms2')
        prodsales_product_service3 = request.form.get('prodsales_product_service3')
        prodsales_sales_vol3 = request.form.get('prodsales_sales_vol3')
        prodsales_unit_selling3 = request.form.get('prodsales_unit_selling3')
        prodsales_unit_measurement3 = request.form.get('prodsales_unit_measurement3')
        prodsales_payment_terms3 = request.form.get('prodsales_payment_terms3')
        direct_farm = request.form.get('direct_farm')
        public_market = request.form.get('public_market')
        trader_conso = request.form.get('trader_conso')
        raw_materials = request.form.get('raw_materials')
        volume_supply = request.form.get('volume_supply')
        quality_requirement = request.form.get('quality_requirement')
        unit_measurement_raw = request.form.get('unit_measurement_raw')
        raw_materials2 = request.form.get('raw_materials2')
        volume_supply2 = request.form.get('volume_supply2')
        quality_requirement2 = request.form.get('quality_requirement2')
        unit_measurement_raw2 = request.form.get('unit_measurement_raw2')
        raw_materials3 = request.form.get('raw_materials3')
        volume_supply3 = request.form.get('volume_supply3')
        quality_requirement3 = request.form.get('quality_requirement3')
        unit_measurement_raw3 = request.form.get('unit_measurement_raw3')
        distrib_point_local_cust = request.form.get('distrib_point_local_cust')
        sales_vol_local_cust = request.form.get('sales_vol_local_cust')
        payment_terms_local_cust = request.form.get('payment_terms_local_cust')
        distrib_point_middleman = request.form.get('distrib_point_middleman')
        sales_vol_middleman = request.form.get('sales_vol_middleman')
        payment_terms_middleman = request.form.get('payment_terms_middleman')
        distrib_point_export = request.form.get('distrib_point_export')
        sales_vol_export = request.form.get('sales_vol_export')
        payment_terms_export = request.form.get('payment_terms_export')
        others_specify_marketing = request.form.get('others_specify_marketing')
        distrib_point_others_specify_marketing = request.form.get('distrib_point_others_specify_marketing')
        sales_vol_others_specify_marketing = request.form.get('sales_vol_others_specify_marketing')
        payment_terms_others_specify_marketing = request.form.get('payment_terms_others_specify_marketing')
        inhouse_num_workers = request.form.get('inhouse_num_workers')
        inhouse_memb_ip_group = request.form.get('inhouse_memb_ip_group')
        inhouse_ave_workdays = request.form.get('inhouse_ave_workdays')
        inhouse_ave_salary = request.form.get('inhouse_ave_salary')
        sub_cont_num_workers = request.form.get('sub_cont_num_workers')
        sub_cont_memb_ip_group = request.form.get('sub_cont_memb_ip_group')
        sub_cont_ave_workdays = request.form.get('sub_cont_ave_workdays')
        sub_cont_ave_salary = request.form.get('sub_cont_ave_salary')
        piece_rate_num_workers = request.form.get('piece_rate_num_workers')
        piece_rate_memb_ip_group = request.form.get('piece_rate_memb_ip_group')
        piece_rate_ave_workdays = request.form.get('piece_rate_ave_workdays')
        piece_rate_ave_salary = request.form.get('piece_rate_ave_salary')
        total_num_workers = request.form.get('total_num_workers')
        total_memb_ip_group = request.form.get('total_memb_ip_group')
        total_ave_workdays = request.form.get('total_ave_workdays')
        total_ave_salary = request.form.get('total_ave_salary')
        form_interprise2 = request.form.get('form_interprise2')
        ifyes_form_interprise = request.form.get('ifyes_form_interprise')
        pricing = request.form.get('pricing')
        ifyes_pricing = request.form.get('ifyes_pricing')
        quality_raw = request.form.get('quality_raw')
        ifyes_quality_raw = request.form.get('ifyes_quality_raw')
        quality_final_prod = request.form.get('quality_final_prod')
        ifyes_quality_final_prod = request.form.get('ifyes_quality_final_prod')
        other_specifyc3 = request.form.get('other_specifyc3')
        existing_comm = request.form.get('existing_comm')
        ifyes_existing_comm = request.form.get('ifyes_existing_comm')
        prov_supp_assis = request.form.get('prov_supp_assis')
        ifyes_prov_supp_assis = request.form.get('ifyes_prov_supp_assis')
        business_prodc3 = request.form.get('business_prodc3')
        ifyes_business_prodc3 = request.form.get('ifyes_business_prodc3')
        ifnoc3 = request.form.get('ifnoc3')
        capability = request.form.get('capability')
        tech_equip = request.form.get('tech_equip')
        access_market = request.form.get('access_market')
        commu_key_part = request.form.get('commu_key_part')
        political = request.form.get('political')
        chamber_commerce = request.form.get('chamber_commerce')
        trade_assoc = request.form.get('trade_assoc')
        coopera = request.form.get('coopera')
        commu_key_part2 = request.form.get('commu_key_part2')
        other_orgs_checkbox = request.form.get('other_orgs_checkbox')
        other_orgs_pls_spec = request.form.get('other_orgs_pls_spec')
        name_org = request.form.get('name_org')
        location_org = request.form.get('location_org')
        member_livelihood = request.form.get('member_livelihood')
        ifyes_member_livelihood = request.form.get('ifyes_member_livelihood')
        what_cluster_industry = request.form.get('what_cluster_industry')



        

        formc_data = db.do("INSERT INTO form_c ( name, position_firm, member_indegenous, sex, age, contact_details, email_add, vc_stakeholders, industry_cluster, pfn_specify, reg_businessname, business_addr, form_interprise, interprise_other, issued_by_business_reg, expired_date_business_reg, issued_by_product_reg, expired_date_product_reg, issued_by_cert_reg, expired_date_cert_reg, issued_by_lic_op, expired_date_lic_op, iso_cert_specific, issued_by_iso_cert, expired_date_iso_cert, issued_by_gapgmp_cert, expired_date_gapgmp_cert, issued_by_organic, expired_date_organic, issued_by_halal, expired_date_halal, other_cert_specify, issued_by_other_cert, expired_date_other_cert, none_of_the_above, type_enterprise, store_capacity_organic, store_capacity_synthetic, potential_organic, potential_synthetic, other_info_organic, other_info_synthetic, store_capacity_pesticides, store_capacity_herbicides, potential_pesticides, potential_herbicides, other_info_pesticides, other_info_herbicides, store_capacity_vermicast_compost, potential_vermicast_compost, other_info_vermicast_compost, store_capacity_seedlings, potential_seedlings, other_info_seedlings, others_specific_products, store_capacity_others_specific_products, potential_others_specific_products, other_info_others_specific_products, area_capacity_drying, potential_exp_drying, other_info_drying, area_capacity_storage_hauling, potential_exp_storage_hauling, other_info_storage_hauling, current_capacity_semi_processing, potential_exp_semi_processing, other_info_semi_processing, current_capacity_final_product, potential_exp_final_product, other_info_final_product, volume_consolidation, potential_consolidation, other_info_consolidation, production_pack_label, potential_pack_label, other_info_pack_label, loan_portfo_micro_financing, potential_micro_financing, other_info_micro_financing, loan_portfo_insurance, potential_insurance, other_info_insurance, prodsales_product_service, prodsales_sales_vol, prodsales_unit_selling, prodsales_unit_measurement,prodsales_payment_terms, prodsales_product_service2, prodsales_sales_vol2, prodsales_unit_selling2, prodsales_unit_measurement2,prodsales_payment_terms2, prodsales_product_service3, prodsales_sales_vol3, prodsales_unit_selling3, prodsales_unit_measurement3,prodsales_payment_terms3, direct_farm, public_market, trader_conso, raw_materials, volume_supply, quality_requirement, unit_measurement_raw, raw_materials2, volume_supply2, quality_requirement2, unit_measurement_raw2, raw_materials3, volume_supply3, quality_requirement3, unit_measurement_raw3, distrib_point_local_cust, sales_vol_local_cust, payment_terms_local_cust, distrib_point_middleman, sales_vol_middleman, payment_terms_middleman, distrib_point_export, sales_vol_export, payment_terms_export, others_specify_marketing, distrib_point_others_specify_marketing, sales_vol_others_specify_marketing, payment_terms_others_specify_marketing, inhouse_num_workers, inhouse_memb_ip_group, inhouse_ave_workdays, inhouse_ave_salary, sub_cont_num_workers, sub_cont_memb_ip_group, sub_cont_ave_workdays, sub_cont_ave_salary, piece_rate_num_workers, piece_rate_memb_ip_group, piece_rate_ave_workdays, piece_rate_ave_salary, total_num_workers, total_memb_ip_group, total_ave_workdays, total_ave_salary, form_interprise2, ifyes_form_interprise, pricing, ifyes_pricing, quality_raw, ifyes_quality_raw, quality_final_prod, ifyes_quality_final_prod, other_specifyc3, existing_comm, ifyes_existing_comm, prov_supp_assis, ifyes_prov_supp_assis, business_prodc3, ifyes_business_prodc3, ifnoc3, capability, tech_equip, access_market, commu_key_part, political, chamber_commerce, trade_assoc, coopera, commu_key_part2, other_orgs_checkbox, other_orgs_pls_spec, name_org, location_org, member_livelihood, ifyes_member_livelihood, what_cluster_industry) VALUES ('{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}','{}', '{}', '{}','{}', '{}', '{}')". 
        format( name, position_firm, member_indegenous, sex, age, contact_details, email_add, vc_stakeholders, industry_cluster, pfn_specify, reg_businessname, business_addr, form_interprise, interprise_other, issued_by_business_reg, expired_date_business_reg, issued_by_product_reg, expired_date_product_reg, issued_by_cert_reg, expired_date_cert_reg, issued_by_lic_op, expired_date_lic_op, iso_cert_specific, issued_by_iso_cert, expired_date_iso_cert, issued_by_gapgmp_cert, expired_date_gapgmp_cert, issued_by_organic, expired_date_organic, issued_by_halal, expired_date_halal, other_cert_specify, issued_by_other_cert, expired_date_other_cert, none_of_the_above, type_enterprise, store_capacity_organic, store_capacity_synthetic, potential_organic, potential_synthetic, other_info_organic, other_info_synthetic, store_capacity_pesticides, store_capacity_herbicides, potential_pesticides, potential_herbicides, other_info_pesticides, other_info_herbicides, store_capacity_vermicast_compost, potential_vermicast_compost, other_info_vermicast_compost, store_capacity_seedlings, potential_seedlings, other_info_seedlings, others_specific_products, store_capacity_others_specific_products, potential_others_specific_products, other_info_others_specific_products, area_capacity_drying, potential_exp_drying, other_info_drying, area_capacity_storage_hauling, potential_exp_storage_hauling, other_info_storage_hauling, current_capacity_semi_processing, potential_exp_semi_processing, other_info_semi_processing, current_capacity_final_product, potential_exp_final_product, other_info_final_product, volume_consolidation, potential_consolidation, other_info_consolidation, production_pack_label, potential_pack_label, other_info_pack_label, loan_portfo_micro_financing, potential_micro_financing, other_info_micro_financing, loan_portfo_insurance, potential_insurance, other_info_insurance, prodsales_product_service, prodsales_sales_vol, prodsales_unit_selling, prodsales_unit_measurement,prodsales_payment_terms, prodsales_product_service2, prodsales_sales_vol2, prodsales_unit_selling2, prodsales_unit_measurement2,prodsales_payment_terms2, prodsales_product_service3, prodsales_sales_vol3, prodsales_unit_selling3, prodsales_unit_measurement3,prodsales_payment_terms3, direct_farm, public_market, trader_conso, raw_materials, volume_supply, quality_requirement, unit_measurement_raw, raw_materials2, volume_supply2, quality_requirement2, unit_measurement_raw2, raw_materials3, volume_supply3, quality_requirement3, unit_measurement_raw3, distrib_point_local_cust, sales_vol_local_cust, payment_terms_local_cust, distrib_point_middleman, sales_vol_middleman, payment_terms_middleman, distrib_point_export, sales_vol_export, payment_terms_export, others_specify_marketing, distrib_point_others_specify_marketing, sales_vol_others_specify_marketing, payment_terms_others_specify_marketing, inhouse_num_workers, inhouse_memb_ip_group, inhouse_ave_workdays, inhouse_ave_salary, sub_cont_num_workers, sub_cont_memb_ip_group, sub_cont_ave_workdays, sub_cont_ave_salary, piece_rate_num_workers, piece_rate_memb_ip_group, piece_rate_ave_workdays, piece_rate_ave_salary, total_num_workers, total_memb_ip_group, total_ave_workdays, total_ave_salary, form_interprise2, ifyes_form_interprise, pricing, ifyes_pricing, quality_raw, ifyes_quality_raw, quality_final_prod, ifyes_quality_final_prod, other_specifyc3, existing_comm, ifyes_existing_comm, prov_supp_assis, ifyes_prov_supp_assis, business_prodc3, ifyes_business_prodc3, ifnoc3, capability, tech_equip, access_market, commu_key_part, political, chamber_commerce, trade_assoc, coopera, commu_key_part2, other_orgs_checkbox, other_orgs_pls_spec, name_org, location_org, member_livelihood, ifyes_member_livelihood, what_cluster_industry))
        #return str(formc_data)
     
        if(formc_data["response"]=="error"):
            flash(f"An error occured !", "error")
        else:
            flash(f"Record Saved!", "success")
    return redirect("/cform")
    


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        position_firm = request.form['position_firm']
        member_indegenous = request.form['member_indegenous']
        sex = request.form.get('sex')
        age = request.form['age']
        contact_details = request.form['contact_details']
        email_add = request.form['email_add']
        vc_stakeholders = request.form.get('vc_stakeholders')
        industry_cluster = request.form.get('industry_cluster')
        pfn_specify = request.form['pfn_specify']
        reg_businessname = request.form['reg_businessname']
        business_addr = request.form['business_addr']
        form_interprise = request.form.get('form_interprise')
        interprise_other = request.form.get('interprise_other')
        issued_by_business_reg = request.form.get('issued_by_business_reg')
        expired_date_business_reg = request.form.get('expired_date_business_reg')
        issued_by_product_reg = request.form.get('issued_by_product_reg')
        expired_date_product_reg = request.form.get('expired_date_product_reg')
        issued_by_cert_reg = request.form.get('issued_by_cert_reg')
        expired_date_cert_reg = request.form.get('expired_date_cert_reg')
        issued_by_lic_op = request.form.get('issued_by_lic_op')
        expired_date_lic_op = request.form.get('expired_date_lic_op')
        iso_cert_specific = request.form.get('iso_cert_specific')
        issued_by_iso_cert = request.form.get('issued_by_iso_cert')
        expired_date_iso_cert = request.form.get('expired_date_iso_cert')
        issued_by_gapgmp_cert = request.form.get('issued_by_gapgmp_cert')
        expired_date_gapgmp_cert = request.form.get('expired_date_gapgmp_cert')
        issued_by_organic = request.form.get('issued_by_organic')
        expired_date_organic = request.form.get('expired_date_organic')
        issued_by_halal = request.form.get('issued_by_halal')
        expired_date_halal = request.form.get('expired_date_halal')
        other_cert_specify = request.form.get('other_cert_specify')
        issued_by_other_cert = request.form.get('issued_by_other_cert')
        expired_date_other_cert = request.form.get('expired_date_other_cert')
        none_of_the_above = request.form.get('none_of_the_above')
        type_enterprise = request.form.get('type_enterprise')
        store_capacity_organic = request.form.get('store_capacity_organic')
        store_capacity_synthetic = request.form.get('store_capacity_synthetic')
        potential_organic = request.form.get('potential_organic')
        potential_synthetic = request.form.get('potential_synthetic')
        other_info_organic = request.form.get('other_info_organic')
        other_info_synthetic = request.form.get('other_info_synthetic')
        store_capacity_pesticides = request.form.get('store_capacity_pesticides')
        store_capacity_herbicides = request.form.get('store_capacity_herbicides')
        potential_pesticides = request.form.get('potential_pesticides')
        potential_herbicides = request.form.get('potential_herbicides')
        other_info_pesticides = request.form.get('other_info_pesticides')
        other_info_herbicides = request.form.get('other_info_herbicides')
        store_capacity_vermicast_compost = request.form.get('store_capacity_vermicast_compost')
        potential_vermicast_compost = request.form.get('potential_vermicast_compost')
        other_info_vermicast_compost = request.form.get('other_info_vermicast_compost')
        store_capacity_seedlings = request.form.get('store_capacity_seedlings')
        potential_seedlings = request.form.get('potential_seedlings')
        other_info_seedlings = request.form.get('other_info_seedlings')
        others_specific_products = request.form.get('others_specific_products')
        store_capacity_others_specific_products = request.form.get('store_capacity_others_specific_products')
        potential_others_specific_products = request.form.get('potential_others_specific_products')
        other_info_others_specific_products = request.form.get('other_info_others_specific_products')
        area_capacity_drying = request.form.get('area_capacity_drying')
        potential_exp_drying = request.form.get('potential_exp_drying')
        other_info_drying = request.form.get('other_info_drying')
        area_capacity_storage_hauling = request.form.get('area_capacity_storage_hauling')
        potential_exp_storage_hauling = request.form.get('potential_exp_storage_hauling')
        other_info_storage_hauling = request.form.get('other_info_storage_hauling')
        current_capacity_semi_processing = request.form.get('current_capacity_semi_processing')
        potential_exp_semi_processing = request.form.get('potential_exp_semi_processing')
        other_info_semi_processing = request.form.get('other_info_semi_processing')
        current_capacity_final_product = request.form.get('current_capacity_final_product')
        potential_exp_final_product = request.form.get('potential_exp_final_product')
        other_info_final_product = request.form.get('other_info_final_product')
        volume_consolidation = request.form.get('volume_consolidation')
        potential_consolidation = request.form.get('potential_consolidation')
        other_info_consolidation = request.form.get('other_info_consolidation')
        production_pack_label = request.form.get('production_pack_label')
        potential_pack_label = request.form.get('potential_pack_label')
        other_info_pack_label = request.form.get('other_info_pack_label')
        loan_portfo_micro_financing = request.form.get('loan_portfo_micro_financing')
        potential_micro_financing = request.form.get('potential_micro_financing')
        other_info_micro_financing = request.form.get('other_info_micro_financing')
        loan_portfo_insurance = request.form.get('loan_portfo_insurance')
        potential_insurance = request.form.get('potential_insurance')
        other_info_insurance = request.form.get('other_info_insurance')
        prodsales_product_service = request.form.get('prodsales_product_service')
        prodsales_sales_vol = request.form.get('prodsales_sales_vol')
        prodsales_unit_selling = request.form.get('prodsales_unit_selling')
        prodsales_unit_measurement = request.form.get('prodsales_unit_measurement')
        prodsales_payment_terms = request.form.get('prodsales_payment_terms')
        prodsales_product_service2 = request.form.get('prodsales_product_service2')
        prodsales_sales_vol2 = request.form.get('prodsales_sales_vol2')
        prodsales_unit_selling2 = request.form.get('prodsales_unit_selling2')
        prodsales_unit_measurement2 = request.form.get('prodsales_unit_measurement2')
        prodsales_payment_terms2 = request.form.get('prodsales_payment_terms2')
        prodsales_product_service3 = request.form.get('prodsales_product_service3')
        prodsales_sales_vol3 = request.form.get('prodsales_sales_vol3')
        prodsales_unit_selling3 = request.form.get('prodsales_unit_selling3')
        prodsales_unit_measurement3 = request.form.get('prodsales_unit_measurement3')
        prodsales_payment_terms3 = request.form.get('prodsales_payment_terms3')
        direct_farm = request.form.get('direct_farm')
        public_market = request.form.get('public_market')
        trader_conso = request.form.get('trader_conso')
        raw_materials = request.form.get('raw_materials')
        volume_supply = request.form.get('volume_supply')
        quality_requirement = request.form.get('quality_requirement')
        unit_measurement_raw = request.form.get('unit_measurement_raw')
        raw_materials2 = request.form.get('raw_materials2')
        volume_supply2 = request.form.get('volume_supply2')
        quality_requirement2 = request.form.get('quality_requirement2')
        unit_measurement_raw2 = request.form.get('unit_measurement_raw2')
        raw_materials3 = request.form.get('raw_materials3')
        volume_supply3 = request.form.get('volume_supply3')
        quality_requirement3 = request.form.get('quality_requirement3')
        unit_measurement_raw3 = request.form.get('unit_measurement_raw3')
        distrib_point_local_cust = request.form.get('distrib_point_local_cust')
        sales_vol_local_cust = request.form.get('sales_vol_local_cust')
        payment_terms_local_cust = request.form.get('payment_terms_local_cust')
        distrib_point_middleman = request.form.get('distrib_point_middleman')
        sales_vol_middleman = request.form.get('sales_vol_middleman')
        payment_terms_middleman = request.form.get('payment_terms_middleman')
        distrib_point_export = request.form.get('distrib_point_export')
        sales_vol_export = request.form.get('sales_vol_export')
        payment_terms_export = request.form.get('payment_terms_export')
        others_specify_marketing = request.form.get('others_specify_marketing')
        distrib_point_others_specify_marketing = request.form.get('distrib_point_others_specify_marketing')
        sales_vol_others_specify_marketing = request.form.get('sales_vol_others_specify_marketing')
        payment_terms_others_specify_marketing = request.form.get('payment_terms_others_specify_marketing')
        inhouse_num_workers = request.form.get('inhouse_num_workers')
        inhouse_memb_ip_group = request.form.get('inhouse_memb_ip_group')
        inhouse_ave_workdays = request.form.get('inhouse_ave_workdays')
        inhouse_ave_salary = request.form.get('inhouse_ave_salary')
        sub_cont_num_workers = request.form.get('sub_cont_num_workers')
        sub_cont_memb_ip_group = request.form.get('sub_cont_memb_ip_group')
        sub_cont_ave_workdays = request.form.get('sub_cont_ave_workdays')
        sub_cont_ave_salary = request.form.get('sub_cont_ave_salary')
        piece_rate_num_workers = request.form.get('piece_rate_num_workers')
        piece_rate_memb_ip_group = request.form.get('piece_rate_memb_ip_group')
        piece_rate_ave_workdays = request.form.get('piece_rate_ave_workdays')
        piece_rate_ave_salary = request.form.get('piece_rate_ave_salary')
        total_num_workers = request.form.get('total_num_workers')
        total_memb_ip_group = request.form.get('total_memb_ip_group')
        total_ave_workdays = request.form.get('total_ave_workdays')
        total_ave_salary = request.form.get('total_ave_salary')
        form_interprise2 = request.form.get('form_interprise2')
        ifyes_form_interprise = request.form.get('ifyes_form_interprise')
        pricing = request.form.get('pricing')
        ifyes_pricing = request.form.get('ifyes_pricing')
        quality_raw = request.form.get('quality_raw')
        ifyes_quality_raw = request.form.get('ifyes_quality_raw')
        quality_final_prod = request.form.get('quality_final_prod')
        ifyes_quality_final_prod = request.form.get('ifyes_quality_final_prod')
        other_specifyc3 = request.form.get('other_specifyc3')
        existing_comm = request.form.get('existing_comm')
        ifyes_existing_comm = request.form.get('ifyes_existing_comm')
        prov_supp_assis = request.form.get('prov_supp_assis')
        ifyes_prov_supp_assis = request.form.get('ifyes_prov_supp_assis')
        business_prodc3 = request.form.get('business_prodc3')
        ifyes_business_prodc3 = request.form.get('ifyes_business_prodc3')
        ifnoc3 = request.form.get('ifnoc3')
        capability = request.form.get('capability')
        tech_equip = request.form.get('tech_equip')
        access_market = request.form.get('access_market')
        commu_key_part = request.form.get('commu_key_part')
        political = request.form.get('political')
        chamber_commerce = request.form.get('chamber_commerce')
        trade_assoc = request.form.get('trade_assoc')
        coopera = request.form.get('coopera')
        commu_key_part2 = request.form.get('commu_key_part2')
        other_orgs_checkbox = request.form.get('other_orgs_checkbox')
        other_orgs_pls_spec = request.form.get('other_orgs_pls_spec')
        name_org = request.form.get('name_org')
        location_org = request.form.get('location_org')
        member_livelihood = request.form.get('member_livelihood')
        ifyes_member_livelihood = request.form.get('ifyes_member_livelihood')
        what_cluster_industry = request.form.get('what_cluster_industry')
        sql = """UPDATE form_c
               SET name='{}', position_firm='{}', member_indegenous='{}', sex='{}', age='{}', contact_details='{}', email_add='{}', vc_stakeholders='{}', industry_cluster='{}', pfn_specify='{}', reg_businessname='{}', business_addr='{}', form_interprise='{}', interprise_other='{}', issued_by_business_reg='{}', expired_date_business_reg='{}', issued_by_product_reg='{}', expired_date_product_reg='{}', issued_by_cert_reg='{}', expired_date_cert_reg='{}', issued_by_lic_op='{}', expired_date_lic_op='{}', iso_cert_specific='{}', issued_by_iso_cert='{}', expired_date_iso_cert='{}',
                issued_by_gapgmp_cert='{}', expired_date_gapgmp_cert='{}', issued_by_organic='{}', expired_date_organic='{}', issued_by_halal='{}', expired_date_halal='{}', other_cert_specify='{}',
                 issued_by_other_cert='{}', expired_date_other_cert='{}', none_of_the_above='{}', type_enterprise='{}', store_capacity_organic='{}', store_capacity_synthetic='{}', potential_organic='{}',
                  potential_synthetic='{}', other_info_organic='{}', other_info_synthetic='{}', store_capacity_pesticides='{}', store_capacity_herbicides='{}', potential_pesticides='{}', potential_herbicides='{}',
                   other_info_pesticides='{}', other_info_herbicides='{}', store_capacity_vermicast_compost='{}', potential_vermicast_compost='{}', other_info_vermicast_compost='{}', store_capacity_seedlings='{}',
                    potential_seedlings='{}', other_info_seedlings='{}', others_specific_products='{}', store_capacity_others_specific_products='{}', potential_others_specific_products='{}',
                     other_info_others_specific_products='{}', area_capacity_drying='{}', potential_exp_drying='{}', other_info_drying='{}', area_capacity_storage_hauling='{}', potential_exp_storage_hauling='{}',
                      other_info_storage_hauling='{}', current_capacity_semi_processing='{}', potential_exp_semi_processing='{}', other_info_semi_processing='{}', current_capacity_final_product='{}',
                       potential_exp_final_product='{}', other_info_final_product='{}', volume_consolidation='{}', potential_consolidation='{}', other_info_consolidation='{}', production_pack_label='{}',
                        potential_pack_label='{}', other_info_pack_label='{}', loan_portfo_micro_financing='{}', potential_micro_financing='{}', other_info_micro_financing='{}', loan_portfo_insurance='{}', 
                        potential_insurance='{}', other_info_insurance='{}', prodsales_product_service='{}', prodsales_sales_vol='{}', prodsales_unit_selling='{}', prodsales_unit_measurement='{}',prodsales_payment_terms='{}',
                         prodsales_product_service2='{}', prodsales_sales_vol2='{}', prodsales_unit_selling2='{}', prodsales_unit_measurement2='{}',prodsales_payment_terms2='{}', prodsales_product_service3='{}', prodsales_sales_vol3='{}', 
                         prodsales_unit_selling3='{}', prodsales_unit_measurement3='{}',prodsales_payment_terms3='{}', direct_farm='{}', public_market='{}', trader_conso='{}', raw_materials='{}', volume_supply='{}', quality_requirement='{}', 
                         unit_measurement_raw='{}', raw_materials2='{}', volume_supply2='{}', quality_requirement2='{}', unit_measurement_raw2='{}', raw_materials3='{}', volume_supply3='{}', quality_requirement3='{}', 
                         unit_measurement_raw3='{}', distrib_point_local_cust='{}', sales_vol_local_cust='{}', payment_terms_local_cust='{}', distrib_point_middleman='{}', sales_vol_middleman='{}', payment_terms_middleman='{}', 
                         distrib_point_export='{}', sales_vol_export='{}', payment_terms_export='{}', others_specify_marketing='{}', distrib_point_others_specify_marketing='{}', sales_vol_others_specify_marketing='{}', 
                         payment_terms_others_specify_marketing='{}', inhouse_num_workers='{}', inhouse_memb_ip_group='{}', inhouse_ave_workdays='{}', inhouse_ave_salary='{}', sub_cont_num_workers='{}', sub_cont_memb_ip_group='{}', 
                         sub_cont_ave_workdays='{}', sub_cont_ave_salary='{}', piece_rate_num_workers='{}', piece_rate_memb_ip_group='{}', piece_rate_ave_workdays='{}', piece_rate_ave_salary='{}', total_num_workers='{}', 
                         total_memb_ip_group='{}', total_ave_workdays='{}', total_ave_salary='{}', form_interprise2='{}', ifyes_form_interprise='{}', pricing='{}', ifyes_pricing='{}', quality_raw='{}', ifyes_quality_raw='{}', quality_final_prod='{}',
                         ifyes_quality_final_prod='{}', other_specifyc3='{}', existing_comm='{}', ifyes_existing_comm='{}', prov_supp_assis='{}', ifyes_prov_supp_assis='{}', business_prodc3='{}', ifyes_business_prodc3='{}', ifnoc3='{}', 
                         capability='{}', tech_equip='{}', access_market='{}', commu_key_part='{}', political='{}', chamber_commerce='{}', trade_assoc='{}', coopera='{}', commu_key_part2='{}', other_orgs_checkbox='{}', other_orgs_pls_spec='{}',
                          name_org='{}', location_org='{}', member_livelihood='{}', ifyes_member_livelihood='{}', what_cluster_industry='{}'
               WHERE id={}
            """.format(name, position_firm, member_indegenous, sex, age, contact_details, email_add, vc_stakeholders, industry_cluster, pfn_specify, reg_businessname, business_addr, form_interprise, interprise_other, issued_by_business_reg, expired_date_business_reg, issued_by_product_reg, expired_date_product_reg, issued_by_cert_reg, expired_date_cert_reg, issued_by_lic_op, expired_date_lic_op, iso_cert_specific, issued_by_iso_cert, expired_date_iso_cert, issued_by_gapgmp_cert, expired_date_gapgmp_cert, issued_by_organic, expired_date_organic, issued_by_halal, expired_date_halal, other_cert_specify, issued_by_other_cert, expired_date_other_cert, none_of_the_above, type_enterprise, store_capacity_organic, store_capacity_synthetic, potential_organic, potential_synthetic, other_info_organic, other_info_synthetic, store_capacity_pesticides, store_capacity_herbicides, potential_pesticides, potential_herbicides, other_info_pesticides, other_info_herbicides, store_capacity_vermicast_compost, potential_vermicast_compost, other_info_vermicast_compost, store_capacity_seedlings, potential_seedlings, other_info_seedlings, others_specific_products, store_capacity_others_specific_products, potential_others_specific_products, other_info_others_specific_products, area_capacity_drying, potential_exp_drying, other_info_drying, area_capacity_storage_hauling, potential_exp_storage_hauling, other_info_storage_hauling, current_capacity_semi_processing, potential_exp_semi_processing, other_info_semi_processing, current_capacity_final_product, potential_exp_final_product, other_info_final_product, volume_consolidation, potential_consolidation, other_info_consolidation, production_pack_label, potential_pack_label, other_info_pack_label, loan_portfo_micro_financing, potential_micro_financing, other_info_micro_financing, loan_portfo_insurance, potential_insurance, other_info_insurance, prodsales_product_service, prodsales_sales_vol, prodsales_unit_selling, prodsales_unit_measurement,prodsales_payment_terms, prodsales_product_service2, prodsales_sales_vol2, prodsales_unit_selling2, prodsales_unit_measurement2,prodsales_payment_terms2, prodsales_product_service3, prodsales_sales_vol3, prodsales_unit_selling3, prodsales_unit_measurement3,prodsales_payment_terms3, direct_farm, public_market, trader_conso, raw_materials, volume_supply, quality_requirement, unit_measurement_raw, raw_materials2, volume_supply2, quality_requirement2, unit_measurement_raw2, raw_materials3, volume_supply3, quality_requirement3, unit_measurement_raw3, distrib_point_local_cust, sales_vol_local_cust, payment_terms_local_cust, distrib_point_middleman, sales_vol_middleman, payment_terms_middleman, distrib_point_export, sales_vol_export, payment_terms_export, others_specify_marketing, distrib_point_others_specify_marketing, sales_vol_others_specify_marketing, payment_terms_others_specify_marketing, inhouse_num_workers, inhouse_memb_ip_group, inhouse_ave_workdays, inhouse_ave_salary, sub_cont_num_workers, sub_cont_memb_ip_group, sub_cont_ave_workdays, sub_cont_ave_salary, piece_rate_num_workers, piece_rate_memb_ip_group, piece_rate_ave_workdays, piece_rate_ave_salary, total_num_workers, total_memb_ip_group, total_ave_workdays, total_ave_salary, form_interprise2, ifyes_form_interprise, pricing, ifyes_pricing, quality_raw, ifyes_quality_raw, quality_final_prod, ifyes_quality_final_prod, other_specifyc3, existing_comm, ifyes_existing_comm, prov_supp_assis, ifyes_prov_supp_assis, business_prodc3, ifyes_business_prodc3, ifnoc3, capability, tech_equip, access_market, commu_key_part, political, chamber_commerce, trade_assoc, coopera, commu_key_part2, other_orgs_checkbox, other_orgs_pls_spec, name_org, location_org, member_livelihood, ifyes_member_livelihood, what_cluster_industry, id)
        db.err_page = "asdasd"
        last_row_update_id = db.do(sql)
        if(last_row_update_id["response"]=="error"):
            flash(f"An error occured !", "error")
        else:
            flash(f"Data Updated! ", "success")
        # return redirect(url_for('formcdashboard'))
        return redirect("/formcdashboard")




@app.route("/formcdashboard")
def formcdashboard():
    if(is_on_session()):
        pass
    else:
        return redirect("/login?force_url=1")
        
    USER_INFO = session["USER_DATA"]
    data_count_entry=db.select("SELECT * FROM form_c")
    datatable=db.select("SELECT * FROM form_c")
    data_lastmonth = db.select("SELECT * FROM form_c WHERE YEAR(date_created) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH) AND MONTH(date_created) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH)")
    data_currmonth= db.select("SELECT * FROM form_c WHERE YEAR(date_created) = YEAR(CURRENT_DATE) AND MONTH(date_created) = MONTH(CURRENT_DATE)")
    data_count_reg_business = db.select("SELECT reg_businessname FROM form_c")
    data_count_position_firm = db.select("SELECT position_firm FROM form_c")
    data_count_cacao = db.select("SELECT * FROM form_c where industry_cluster = 'cacao'")
    data_count_coffee = db.select("SELECT * FROM form_c where industry_cluster = 'coffee'")
    data_count_coconut = db.select("SELECT * FROM form_c where industry_cluster = 'coconut'")
    data_count_pfn = db.select("SELECT `pfn_specify` FROM form_c WHERE `pfn_specify` != '' OR `pfn_specify` != ' ' ;")
    thismonth=len(data_currmonth)
    lastmonth=len(data_lastmonth)
    subperc= thismonth - lastmonth
    percentage= (subperc / lastmonth)
    print(lastmonth)
    print(thismonth)
    print(subperc)
    all = data_count_cacao + data_count_coffee + data_count_coconut + data_count_pfn
    return render_template("formcdashboard.html",count_entry=len(data_count_entry), tabledata=data_count_entry, count_reg_business=len(data_count_reg_business), 
    count_position_firm=len(data_count_position_firm), count_cacao=len(data_count_cacao), count_coffee=len(data_count_coffee), count_pfn=len(data_count_pfn),
    count_coconut=len(data_count_coconut), datatable=datatable, data_lastmonth=len(data_lastmonth), data_currmonth=len(data_currmonth),percentage = round(percentage,2),USER_INFO=USER_INFO)

@app.route("/formcdashboardfilter",methods=['POST','GET'])
def formcdashboardfilter():
    if request.method == 'POST':
        filter1 = request.form.get('filter1')
        filter2 = request.form.get('filter2')
        filter3 = request.form.get('filter3')
        filter4 = request.form.get('filter4')
    # filtering industry cluster - form enterprise
    datatable=db.select("SELECT * FROM form_c")
    coffee_singlesolesql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='coffee' AND form_interprise='Single/Sole'")
    cacao_singlesolesql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='cacao' AND form_interprise='Single/Sole'")
    coconut_singlesolesql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='coconut' AND form_interprise='Single/Sole'")
    pfn_singlesolesql=db.select("SELECT `pfn_specify`,`form_interprise` from form_c where pfn_specify !='' AND form_interprise='Single/Sole'")

    coffee_partnershipsql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='coffee' AND form_interprise='partnership'")
    cacao_partnershipsql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='cacao' AND form_interprise='partnership'")
    coconut_partnershipsql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='coconut' AND form_interprise='partnership'")
    pfn_partnershipsql=db.select("SELECT `pfn_specify`,`form_interprise` from form_c where pfn_specify !='' AND form_interprise='partnership'")

    coffee_corporationsql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='coffee' AND form_interprise='corporation'")
    cacao_corporationsql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='cacao' AND form_interprise='corporation'")
    coconut_corporationsql=db.select("SELECT `industry_cluster`,`form_interprise` from form_c where industry_cluster='coconut' AND form_interprise='corporation'")
    pfn_corporationsql=db.select("SELECT `pfn_specify`,`form_interprise` from form_c where pfn_specify !='' AND form_interprise='corporation'")

    coffee_otherql=db.select("SELECT `industry_cluster`,`interprise_other` from form_c where industry_cluster='coffee' AND interprise_other != '' ")
    cacao_othersql=db.select("SELECT `industry_cluster`,`interprise_other` from form_c where industry_cluster='cacao' AND interprise_other != '' ")
    coconut_othersql=db.select("SELECT `industry_cluster`,`interprise_other` from form_c where industry_cluster='coconut' AND interprise_other != '' ")
    pfn_othersql=db.select("SELECT `pfn_specify`,`interprise_other` from form_c where pfn_specify !='' AND interprise_other != '' ")
    #------------------------------------

    # filtering gender - form enterprise
    male_singlesolesql=db.select("SELECT * from form_c where sex='male' AND form_interprise='Single/Sole'")
    female_singlesolesql=db.select("SELECT * from form_c where sex='female'  AND form_interprise='Single/Sole'")

    male_partnershipsql=db.select("SELECT `sex`,`form_interprise` from form_c where sex='male' AND form_interprise='Partnership'")
    female_partnershipsql=db.select("SELECT `sex`,`form_interprise` from form_c where sex='female'  AND form_interprise='Partnership'")

    male_corporationsql=db.select("SELECT `sex`,`form_interprise` from form_c where sex='male' AND form_interprise='corporation'")
    female_corporationsql=db.select("SELECT `sex`,`form_interprise` from form_c where sex='female'  AND form_interprise='corporation'")

    male_othersql=db.select("SELECT `sex`,`interprise_other` from form_c where sex='male' AND interprise_other != ''")
    female_othersql=db.select("SELECT `sex`,`interprise_other` from form_c where sex='female' AND interprise_other != ''")
    #------------------------------------

    # filtering form enterprise - business address
    adn_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%agusan del norte%' AND form_interprise='Single/Sole'")
    ads_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%agusan del sur%' AND form_interprise='Single/Sole'")
    sds_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%surigao del sur%' AND form_interprise='Single/Sole'")
    magui_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%maguindanao%' AND form_interprise='Single/Sole'")
    ns_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%northern samar%' AND form_interprise='Single/Sole'")
    leyte_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE 'leyte%' AND form_interprise='Single/Sole'")
    sleyte_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%southern leyte%' AND form_interprise='Single/Sole'")
    mo_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%misamis oriental%' AND form_interprise='Single/Sole'")
    bukd_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%bukidnon%' AND form_interprise='Single/Sole'")
    ldn_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%lanao del norte%' AND form_interprise='Single/Sole'")
    nc_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%north cotabato%' AND form_interprise='Single/Sole'")
    sk_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%sultan kudarat%' AND form_interprise='Single/Sole'")
    srng_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%sarangani%' AND form_interprise='Single/Sole'")
    zdn_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga del norte%' AND form_interprise='Single/Sole'")
    zs_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga sibugay%' AND form_interprise='Single/Sole'")
    zds_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga del sur%' AND form_interprise='Single/Sole'")
    ddo_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao de oro%' AND form_interprise='Single/Sole'")
    do_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao oriental%' AND form_interprise='Single/Sole'")
    ddn_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao del norte%' AND form_interprise='Single/Sole'")
    dds_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao del sur%' AND form_interprise='Single/Sole'")
    doc_singlesql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao occidental%' AND form_interprise='Single/Sole'")

    adn_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%agusan del norte%' AND form_interprise='partnership'")
    ads_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%agusan del sur%' AND form_interprise='partnership'")
    sds_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%surigao del sur%' AND form_interprise='partnership'")
    magui_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%maguindanao%' AND form_interprise='partnership'")
    ns_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%northern samar%' AND form_interprise='partnership'")
    leyte_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE 'leyte%' AND form_interprise='partnership'")
    sleyte_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%southern leyte%' AND form_interprise='partnership'")
    mo_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%misamis oriental%' AND form_interprise='partnership'")
    bukd_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%bukidnon%' AND form_interprise='partnership'")
    ldn_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%lanao del norte%' AND form_interprise='partnership'")
    nc_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%north cotabato%' AND form_interprise='partnership'")
    sk_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%sultan kudarat%' AND form_interprise='partnership'")
    srng_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%sarangani%' AND form_interprise='partnership'")
    zdn_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga del norte%' AND form_interprise='partnership'")
    zs_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga sibugay%' AND form_interprise='partnership'")
    zds_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga del sur%' AND form_interprise='partnership'")
    ddo_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao de oro%' AND form_interprise='partnership'")
    do_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao oriental%' AND form_interprise='partnership'")
    ddn_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao del norte%' AND form_interprise='partnership'")
    dds_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao del sur%' AND form_interprise='partnership'")
    doc_partsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao occidental%' AND form_interprise='partnership'")

    adn_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%agusan del norte%' AND form_interprise='corporation'")
    ads_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%agusan del sur%' AND form_interprise='corporation'")
    sds_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%surigao del sur%' AND form_interprise='corporation'")
    magui_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%maguindanao%' AND form_interprise='corporation'")
    ns_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%northern samar%' AND form_interprise='corporation'")
    leyte_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE 'leyte%' AND form_interprise='corporation'")
    sleyte_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%southern leyte%' AND form_interprise='corporation'")
    mo_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%misamis oriental%' AND form_interprise='corporation'")
    bukd_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%bukidnon%' AND form_interprise='corporation'")
    ldn_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%lanao del norte%' AND form_interprise='corporation'")
    nc_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%north cotabato%' AND form_interprise='corporation'")
    sk_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%sultan kudarat%' AND form_interprise='corporation'")
    srng_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%sarangani%' AND form_interprise='corporation'")
    zdn_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga del norte%' AND form_interprise='corporation'")
    zs_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga sibugay%' AND form_interprise='corporation'")
    zds_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%zamboanga del sur%' AND form_interprise='corporation'")
    ddo_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao de oro%' AND form_interprise='corporation'")
    do_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao oriental%' AND form_interprise='corporation'")
    ddn_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao del norte%' AND form_interprise='corporation'")
    dds_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao del sur%' AND form_interprise='corporation'")
    doc_corpsql=db.select("SELECT `business_addr`,`form_interprise` from form_c where business_addr LIKE '%davao occidental%' AND form_interprise='corporation'")

    adn_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%agusan del norte%' AND interprise_other != '' ")
    ads_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%agusan del sur%' AND interprise_other != '' ")
    sds_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%surigao del sur%' AND interprise_other != '' ")
    magui_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%maguindanao%' AND interprise_other != '' ")
    ns_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%northern samar%' AND interprise_other != '' ")
    leyte_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE 'leyte%' AND interprise_other != '' ")
    sleyte_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%southern leyte%' AND interprise_other != '' ")
    mo_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%misamis oriental%' AND interprise_other != '' ")
    bukd_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%bukidnon%' AND interprise_other != '' ")
    ldn_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%lanao del norte%' AND interprise_other != '' ")
    nc_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%north cotabato%' AND interprise_other != '' ")
    sk_othersqll=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%sultan kudarat%' AND interprise_other != '' ")
    srng_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%sarangani%' AND interprise_other != '' ")
    zdn_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%zamboanga del norte%' AND interprise_other != '' ")
    zs_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%zamboanga sibugay%' AND interprise_other != '' ")
    zds_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%zamboanga del sur%' AND interprise_other != '' ")
    ddo_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%davao de oro%' AND interprise_other != '' ")
    do_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%davao oriental%' AND interprise_other != '' ")
    ddn_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%davao del norte%' AND interprise_other != '' ")
    dds_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%davao del sur%' AND interprise_other != '' ")
    doc_othersql=db.select("SELECT `business_addr`,`interprise_other` from form_c where business_addr LIKE '%davao occidental%' AND interprise_other != '' ")
    #------------------------------------

     # filtering industry cluster - gender
    coffee_malesql=db.select("SELECT `industry_cluster`,`sex` from form_c where industry_cluster='coffee' AND sex='male'")
    cacao_malesql=db.select("SELECT `industry_cluster`,`sex` from form_c where industry_cluster='cacao' AND sex='male'")
    coconut_malesql=db.select("SELECT `industry_cluster`,`sex` from form_c where industry_cluster='coconut' AND sex='male'")
    pfn_malesql=db.select("SELECT `pfn_specify`,`sex` from form_c where pfn_specify !='' AND sex='male'")

    coffee_femalesql=db.select("SELECT `industry_cluster`,`sex` from form_c where industry_cluster='coffee' AND sex='female'")
    cacao_femalesql=db.select("SELECT `industry_cluster`,`sex` from form_c where industry_cluster='cacao' AND sex='female'")
    coconut_femalesql=db.select("SELECT `industry_cluster`,`sex` from form_c where industry_cluster='coconut' AND sex='female'")
    pfn_femalesql=db.select("SELECT `pfn_specify`,`sex` from form_c where pfn_specify !='' AND sex='female'")
    #----------------------------------------

    # filtering gender - business address
    adn_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%agusan del norte%' AND sex='male'")
    ads_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%agusan del sur%' AND sex='male'")
    sds_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%surigao del sur%' AND sex='male'")
    magui_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%maguindanao%' AND sex='male'")
    ns_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%northern samar%' AND sex='male'")
    leyte_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE 'leyte%' AND sex='male'")
    sleyte_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%southern leyte%' AND sex='male'")
    mo_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%misamis oriental%' AND sex='male'")
    bukd_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%bukidnon%' AND sex='male'")
    ldn_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%lanao del norte%' AND sex='male'")
    nc_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%north cotabato%' AND sex='male'")
    sk_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%sultan kudarat%' AND sex='male'")
    srng_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%sarangani%' AND sex='male'")
    zdn_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%zamboanga del norte%' AND sex='male'")
    zs_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%zamboanga sibugay%' AND sex='male'")
    zds_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%zamboanga del sur%' AND sex='male'")
    ddo_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao de oro%' AND sex='male'")
    do_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao oriental%' AND sex='male'")
    ddn_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao del norte%' AND sex='male'")
    dds_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao del sur%' AND sex='male'")
    doc_malesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao occidental%' AND sex='male'")

    adn_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%agusan del norte%' AND sex='female'")
    ads_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%agusan del sur%' AND sex='female'")
    sds_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%surigao del sur%' AND sex='female'")
    magui_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%maguindanao%' AND sex='female'")
    ns_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%northern samar%' AND sex='female'")
    leyte_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE 'leyte%' AND sex='female'")
    sleyte_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%southern leyte%' AND sex='female'")
    mo_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%misamis oriental%' AND sex='female'")
    bukd_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%bukidnon%' AND sex='female'")
    ldn_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%lanao del norte%' AND sex='female'")
    nc_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%north cotabato%' AND sex='female'")
    sk_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%sultan kudarat%' AND sex='female'")
    srng_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%sarangani%' AND sex='female'")
    zdn_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%zamboanga del norte%' AND sex='female'")
    zs_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%zamboanga sibugay%' AND sex='female'")
    zds_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%zamboanga del sur%' AND sex='female'")
    ddo_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao de oro%' AND sex='female'")
    do_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao oriental%' AND sex='female'")
    ddn_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao del norte%' AND sex='female'")
    dds_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao del sur%' AND sex='female'")
    doc_femalesql=db.select("SELECT `business_addr`,`sex` from form_c where business_addr LIKE '%davao occidental%' AND sex='female'")
    #----------------------------------------

     # filtering industry cluster - business address
    adn_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%agusan del norte%' AND industry_cluster='coffee'")
    ads_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%agusan del sur%' AND industry_cluster='coffee'")
    sds_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%surigao del sur%' AND industry_cluster='coffee'")
    magui_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%maguindanao%' AND industry_cluster='coffee'")
    ns_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%northern samar%' AND industry_cluster='coffee'")
    leyte_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE 'leyte%' AND industry_cluster='coffee'")
    sleyte_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%southern leyte%' AND industry_cluster='coffee'")
    mo_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%misamis oriental%' AND industry_cluster='coffee'")
    bukd_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%bukidnon%' AND industry_cluster='coffee'")
    ldn_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%lanao del norte%' AND industry_cluster='coffee'")
    nc_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%north cotabato%' AND industry_cluster='coffee'")
    sk_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%sultan kudarat%' AND industry_cluster='coffee'")
    srng_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%sarangani%' AND industry_cluster='coffee'")
    zdn_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga del norte%' AND industry_cluster='coffee'")
    zs_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga sibugay%' AND industry_cluster='coffee'")
    zds_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga del sur%' AND industry_cluster='coffee'")
    ddo_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao de oro%' AND industry_cluster='coffee'")
    do_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao oriental%' AND industry_cluster='coffee'")
    ddn_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao del norte%' AND industry_cluster='coffee'")
    dds_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao del sur%' AND industry_cluster='coffee'")
    doc_coffeesql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao occidental%' AND industry_cluster='coffee'")

    adn_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%agusan del norte%' AND industry_cluster='cacao'")
    ads_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%agusan del sur%' AND industry_cluster='cacao'")
    sds_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%surigao del sur%' AND industry_cluster='cacao'")
    magui_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%maguindanao%' AND industry_cluster='cacao'")
    ns_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%northern samar%' AND industry_cluster='cacao'")
    leyte_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE 'leyte%' AND industry_cluster='cacao'")
    sleyte_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%southern leyte%' AND industry_cluster='cacao'")
    mo_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%misamis oriental%' AND industry_cluster='cacao'")
    bukd_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%bukidnon%' AND industry_cluster='cacao'")
    ldn_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%lanao del norte%' AND industry_cluster='cacao'")
    nc_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%north cotabato%' AND industry_cluster='cacao'")
    sk_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%sultan kudarat%' AND industry_cluster='cacao'")
    srng_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%sarangani%' AND industry_cluster='cacao'")
    zdn_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga del norte%' AND industry_cluster='cacao'")
    zs_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga sibugay%' AND industry_cluster='cacao'")
    zds_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga del sur%' AND industry_cluster='cacao'")
    ddo_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao de oro%' AND industry_cluster='cacao'")
    do_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao oriental%' AND industry_cluster='cacao'")
    ddn_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao del norte%' AND industry_cluster='cacao'")
    dds_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao del sur%' AND industry_cluster='cacao'")
    doc_cacaosql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao occidental%' AND industry_cluster='cacao'")

    adn_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%agusan del norte%' AND industry_cluster='coconut'")
    ads_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%agusan del sur%' AND industry_cluster='coconut'")
    sds_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%surigao del sur%' AND industry_cluster='coconut'")
    magui_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%maguindanao%' AND industry_cluster='coconut'")
    ns_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%northern samar%' AND industry_cluster='coconut'")
    leyte_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE 'leyte%' AND industry_cluster='coconut'")
    sleyte_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%southern leyte%' AND industry_cluster='coconut'")
    mo_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%misamis oriental%' AND industry_cluster='coconut'")
    bukd_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%bukidnon%' AND industry_cluster='coconut'")
    ldn_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%lanao del norte%' AND industry_cluster='coconut'")
    nc_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%north cotabato%' AND industry_cluster='coconut'")
    sk_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%sultan kudarat%' AND industry_cluster='coconut'")
    srng_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%sarangani%' AND industry_cluster='coconut'")
    zdn_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga del norte%' AND industry_cluster='coconut'")
    zs_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga sibugay%' AND industry_cluster='coconut'")
    zds_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%zamboanga del sur%' AND industry_cluster='coconut'")
    ddo_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao de oro%' AND industry_cluster='coconut'")
    do_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao oriental%' AND industry_cluster='coconut'")
    ddn_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao del norte%' AND industry_cluster='coconut'")
    dds_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao del sur%' AND industry_cluster='coconut'")
    doc_coconutsql=db.select("SELECT `business_addr`,`industry_cluster` from form_c where business_addr LIKE '%davao occidental%' AND industry_cluster='coconut'")

    adn_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%agusan del norte%' AND pfn_specify!=''")
    ads_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%agusan del sur%' AND pfn_specify!=''")
    sds_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%surigao del sur%' AND pfn_specify!=''")
    magui_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%maguindanao%' AND pfn_specify!=''")
    ns_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%northern samar%' AND pfn_specify!=''")
    leyte_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE 'leyte%' AND pfn_specify!=''")
    sleyte_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%southern leyte%' AND pfn_specify!=''")
    mo_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%misamis oriental%' AND pfn_specify!=''")
    bukd_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%bukidnon%' AND pfn_specify!=''")
    ldn_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%lanao del norte%' AND pfn_specify!=''")
    nc_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%north cotabato%' AND pfn_specify!=''")
    sk_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%sultan kudarat%' AND pfn_specify!=''")
    srng_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%sarangani%' AND pfn_specify!=''")
    zdn_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%zamboanga del norte%' AND pfn_specify!=''")
    zs_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%zamboanga sibugay%' AND pfn_specify!=''")
    zds_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%zamboanga del sur%' AND pfn_specify!=''")
    ddo_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%davao de oro%' AND pfn_specify!=''")
    do_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%davao oriental%' AND pfn_specify!=''")
    ddn_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%davao del norte%' AND pfn_specify!=''")
    dds_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%davao del sur%' AND pfn_specify!=''")
    doc_pfnsql=db.select("SELECT `business_addr`,`pfn_specify` from form_c where business_addr LIKE '%davao occidental%' AND pfn_specify!=''")
    #----------------------------------------


    return render_template("formcdashboardfilter.html",count_male_singlesole=len(male_singlesolesql),count_female_singlesole=len(female_singlesolesql),count_malepartnership=len(male_partnershipsql),
    count_femalepartnership=len(female_partnershipsql),count_male_corporation=len(male_corporationsql),count_female_corporation=len(female_corporationsql),totalsinglesole=len(male_singlesolesql + female_singlesolesql),
    totalpartnership=len(male_partnershipsql + female_partnershipsql),totalcorporation=len(male_corporationsql + female_corporationsql),count_male_other=len(male_othersql)
    ,count_female_other=len(female_othersql),totalother=len(male_othersql + female_othersql), filter1=filter1,filter2=filter2,filter3=filter3,filter4=filter4,
    count_coffee_single=len(coffee_singlesolesql),count_cacao_single=len(cacao_singlesolesql),count_coconut_single=len(coconut_singlesolesql),count_pfn_single=len(pfn_singlesolesql),
    total_industrysingle=len(coffee_singlesolesql+cacao_singlesolesql+coconut_singlesolesql+pfn_singlesolesql),
    count_coffeepart=len(coffee_partnershipsql),count_cacaopart=len(cacao_partnershipsql),count_coconutpart=len(coconut_partnershipsql),count_pfnpart=len(pfn_partnershipsql),
    total_industrypart=len(coffee_partnershipsql+cacao_partnershipsql+coconut_partnershipsql+pfn_partnershipsql),
    count_coffeecorp=len(coffee_corporationsql),count_cacaocorp=len(cacao_corporationsql),count_coconutcorp=len(coconut_corporationsql),count_pfncorp=len(pfn_corporationsql),
    total_industrycorp=len(coffee_corporationsql+cacao_corporationsql+coconut_corporationsql+pfn_corporationsql),
    count_coffeeoth=len(coffee_otherql),count_cacaooth=len(cacao_othersql),count_coconutoth=len(coconut_othersql),count_pfnoth=len(pfn_othersql),
    total_industryoth=len(coffee_otherql+cacao_othersql+coconut_othersql+pfn_othersql), adn_singlesql=len(adn_singlesql), ads_singlesql=len(ads_singlesql),
    sds_singlesql=len(sds_singlesql),magui_singlesql=len(magui_singlesql),ns_singlesql=len(ns_singlesql),leyte_singlesql=len(leyte_singlesql),sleyte_singlesql=len(sleyte_singlesql),
    mo_singlesql=len(mo_singlesql), bukd_singlesql=len(bukd_singlesql), ldn_singlesql=len(ldn_singlesql), nc_singlesql=len(nc_singlesql), sk_singlesql=len(sk_singlesql), srng_singlesql=len(srng_singlesql),
    zdn_singlesql=len(zdn_singlesql),zs_singlesql=len(zs_singlesql),zds_singlesql=len(zds_singlesql),ddo_singlesql=len(ddo_singlesql),do_singlesql=len(do_singlesql),
    ddn_singlesql=len(ddn_singlesql), dds_singlesql=len(dds_singlesql), doc_singlesql=len(doc_singlesql),total_addrsingle=len(adn_singlesql+ads_singlesql+sds_singlesql+magui_singlesql+ns_singlesql+leyte_singlesql
    +sleyte_singlesql+mo_singlesql+bukd_singlesql+ldn_singlesql+nc_singlesql+sk_singlesql+srng_singlesql+zdn_singlesql+zs_singlesql+zds_singlesql+ddo_singlesql+do_singlesql+ddn_singlesql+
    dds_singlesql+doc_singlesql), adn_partsql=len(adn_partsql),ads_partsql=len(ads_partsql),sds_partsql=len(sds_partsql),magui_partsql=len(magui_partsql),ns_partsql=len(ns_partsql),
    leyte_partsql=len(leyte_partsql),sleyte_partsql=len(sleyte_partsql),mo_partsql=len(mo_partsql),bukd_partsql=len(bukd_partsql),ldn_partsql=len(ldn_partsql),nc_partsql=len(nc_partsql),
    sk_partsql=len(sk_partsql),srng_partsql=len(srng_partsql),zdn_partsql=len(zdn_partsql),zs_partsql=len(zs_partsql),zds_partsql=len(zds_partsql),ddo_partsql=len(ddo_partsql),do_partsql=len(do_partsql),
    ddn_partsql=len(ddn_partsql),dds_partsql=len(dds_partsql), doc_partsql=len(doc_partsql), total_addrpart=len(adn_partsql+ads_partsql+sds_partsql+magui_partsql+ns_partsql+
    leyte_partsql+sleyte_partsql+mo_partsql+bukd_partsql+ldn_partsql+nc_partsql+sk_partsql+srng_partsql+zdn_partsql+zs_partsql+zds_partsql+ddo_partsql+do_partsql+ddn_partsql+dds_partsql+doc_partsql),
    adn_corpsql=len(adn_corpsql),ads_corpsql=len(ads_corpsql),sds_corpsql=len(sds_corpsql),magui_corpsql=len(magui_corpsql),ns_corpsql=len(ns_corpsql),
    leyte_corpsql=len(leyte_corpsql),sleyte_corpsql=len(sleyte_corpsql),mo_corpsql=len(mo_corpsql),bukd_corpsql=len(bukd_corpsql),ldn_corpsql=len(ldn_corpsql),nc_corpsql=len(nc_corpsql),
    sk_corpsql=len(sk_corpsql),srng_corpsql=len(srng_corpsql),zdn_corpsql=len(zdn_corpsql),zs_corpsql=len(zs_corpsql),zds_corpsql=len(zds_corpsql),ddo_corpsql=len(ddo_corpsql),do_corpsql=len(do_corpsql),
    ddn_corpsql=len(ddn_corpsql),dds_corpsql=len(dds_corpsql), doc_corpsql=len(doc_corpsql),total_addrcorp=len(adn_corpsql+ads_corpsql+sds_corpsql+magui_corpsql+ns_corpsql+
    leyte_corpsql+sleyte_corpsql+mo_corpsql+bukd_corpsql+ldn_corpsql+nc_corpsql+sk_corpsql+srng_corpsql+zdn_corpsql+zs_corpsql+zds_corpsql+ddo_corpsql+do_corpsql+ddn_corpsql+dds_corpsql+doc_corpsql),
    coffee_malesql=len(coffee_malesql),cacao_malesql=len(cacao_malesql),coconut_malesql=len(coconut_malesql),pfn_malesql=len(pfn_malesql), coffee_femalesql=len(coffee_femalesql),
    cacao_femalesql=len(cacao_femalesql),coconut_femalesql=len(coconut_femalesql),pfn_femalesql=len(pfn_femalesql), total_coffeegender=len(coffee_malesql+coffee_femalesql), total_cacaogender=len(cacao_malesql+cacao_femalesql),
    total_coconutgender=len(coconut_malesql+coconut_femalesql),total_pfngender=len(pfn_malesql+pfn_femalesql),adn_malesql=len(adn_malesql),ads_malesql=len(ads_malesql),sds_malesql=len(sds_malesql),
    magui_malesql=len(magui_malesql),ns_malesql=len(ns_malesql),leyte_malesql=len(leyte_malesql),sleyte_malesql=len(sleyte_malesql),mo_malesql=len(mo_malesql),bukd_malesql=len(bukd_malesql),
    ldn_malesql=len(ldn_malesql),nc_malesql=len(nc_malesql),sk_malesql=len(sk_malesql),srng_malesql=len(srng_malesql),zdn_malesql=len(zdn_malesql),zs_malesql=len(zs_malesql),zds_malesql=len(zds_malesql),
    ddo_malesql=len(ddo_malesql),do_malesql=len(do_malesql),ddn_malesql=len(ddn_malesql),dds_malesql=len(dds_malesql),doc_malesql=len(doc_malesql),adn_femalesql=len(adn_femalesql),ads_femalesql=len(ads_femalesql),sds_femalesql=len(sds_femalesql),
    magui_femalesql=len(magui_femalesql),ns_femalesql=len(ns_femalesql),leyte_femalesql=len(leyte_femalesql),sleyte_femalesql=len(sleyte_femalesql),mo_femalesql=len(mo_femalesql),bukd_femalesql=len(bukd_femalesql),
    ldn_femalesql=len(ldn_femalesql),nc_femalesql=len(nc_femalesql),sk_femalesql=len(sk_femalesql),srng_femalesql=len(srng_femalesql),zdn_femalesql=len(zdn_femalesql),zs_femalesql=len(zs_femalesql),zds_femalesql=len(zds_femalesql),
    ddo_femalesql=len(ddo_femalesql),do_femaleql=len(do_femalesql),ddn_femalesql=len(ddn_femalesql),dds_femalesql=len(dds_femalesql),doc_femalesql=len(doc_femalesql),
    total_maleaddr=len(adn_malesql+ads_malesql+sds_malesql+magui_malesql+ns_malesql+leyte_malesql+sleyte_malesql+mo_malesql+bukd_malesql+ldn_malesql+nc_malesql+sk_malesql+srng_malesql+
    zdn_malesql+zs_malesql+zds_malesql+ddo_malesql+do_malesql+ddn_malesql+dds_malesql+doc_malesql),total_femaleaddr=len(adn_femalesql+ads_femalesql+sds_femalesql+
    magui_femalesql+ns_femalesql+leyte_femalesql+sleyte_femalesql+mo_femalesql+bukd_femalesql+ldn_femalesql+nc_femalesql+sk_femalesql+srng_femalesql+
    zdn_femalesql+zs_femalesql+zds_femalesql+ddo_femalesql+do_femalesql+ddn_femalesql+dds_femalesql+doc_femalesql),adn_coffeesql=len(adn_coffeesql),ads_coffeesql=len(ads_coffeesql),sds_coffeesql=len(sds_coffeesql),
    magui_coffeesql=len(magui_coffeesql),ns_coffeesql=len(ns_coffeesql),leyte_coffeesql=len(leyte_coffeesql),sleyte_coffeesql=len(sleyte_coffeesql),mo_coffeesql=len(mo_coffeesql),bukd_coffeesql=len(bukd_coffeesql),
    ldn_coffeesql=len(ldn_coffeesql),nc_coffeesql=len(nc_coffeesql),sk_coffeesql=len(sk_coffeesql),srng_coffeesql=len(srng_coffeesql),zdn_coffeesql=len(zdn_coffeesql),zs_coffeesql=len(zs_coffeesql),zds_coffeesql=len(zds_coffeesql),
    ddo_coffeesql=len(ddo_coffeesql),do_coffeesql=len(do_coffeesql),ddn_coffeesql=len(ddn_coffeesql),dds_coffeesql=len(dds_coffeesql),doc_coffeesql=len(doc_coffeesql),adn_cacaosql=len(adn_cacaosql),ads_cacaosql=len(ads_cacaosql),sds_cacaosql=len(sds_cacaosql),
    magui_cacaosql=len(magui_cacaosql),ns_cacaosql=len(ns_cacaosql),leyte_cacaosql=len(leyte_cacaosql),sleyte_cacaosql=len(sleyte_cacaosql),mo_cacaosql=len(mo_cacaosql),bukd_cacaosql=len(bukd_cacaosql),
    ldn_cacaosql=len(ldn_cacaosql),nc_cacaosql=len(nc_cacaosql),sk_cacaosql=len(sk_cacaosql),srng_cacaosql=len(srng_cacaosql),zdn_cacaosql=len(zdn_cacaosql),zs_cacaosql=len(zs_cacaosql),zds_cacaosql=len(zds_cacaosql),
    ddo_cacaosql=len(ddo_cacaosql),do_cacaosql=len(do_cacaosql),ddn_cacaosql=len(ddn_cacaosql),dds_cacaosql=len(dds_cacaosql),doc_cacaosql=len(doc_cacaosql),adn_coconutsql=len(adn_coconutsql),ads_coconutsql=len(ads_coconutsql),sds_coconutsql=len(sds_coconutsql),
    magui_coconutsql=len(magui_coconutsql),ns_coconutsql=len(ns_coconutsql),leyte_coconutsql=len(leyte_coconutsql),sleyte_coconutsql=len(sleyte_coconutsql),mo_coconutsql=len(mo_coconutsql),bukd_coconutsql=len(bukd_coconutsql),
    ldn_coconutsql=len(ldn_coconutsql),nc_coconutsql=len(nc_coconutsql),sk_coconutsql=len(sk_coconutsql),srng_coconutsql=len(srng_coconutsql),zdn_coconutsql=len(zdn_coconutsql),zs_coconutsql=len(zs_coconutsql),zds_coconutsql=len(zds_coconutsql),
    ddo_coconutsql=len(ddo_coconutsql),do_coconutsql=len(do_coconutsql),ddn_coconutsql=len(ddn_coconutsql),dds_coconutsql=len(dds_coconutsql),doc_coconutsql=len(doc_coconutsql),adn_pfnsql=len(adn_pfnsql),ads_pfnsql=len(ads_pfnsql),sds_pfnsql=len(sds_pfnsql),
    magui_pfnsql=len(magui_pfnsql),ns_pfnsql=len(ns_pfnsql),leyte_pfnsql=len(leyte_pfnsql),sleyte_pfnsql=len(sleyte_pfnsql),mo_pfnsql=len(mo_pfnsql),bukd_pfnsql=len(bukd_pfnsql),
    ldn_pfnsql=len(ldn_pfnsql),nc_pfnsql=len(nc_pfnsql),sk_pfnsql=len(sk_pfnsql),srng_pfnsql=len(srng_pfnsql),zdn_pfnsql=len(zdn_pfnsql),zs_pfnsql=len(zs_pfnsql),zds_pfnsql=len(zds_pfnsql),
    ddo_pfnsql=len(ddo_pfnsql),do_pfnsql=len(do_pfnsql),ddn_pfnsql=len(ddn_pfnsql),dds_pfnsql=len(dds_pfnsql),doc_pfnsql=len(doc_pfnsql),total_coffeeaddr=len(adn_coffeesql+ads_coffeesql+sds_coffeesql+
    magui_coffeesql+ns_coffeesql+leyte_coffeesql+sleyte_coffeesql+mo_coffeesql+bukd_coffeesql+
    ldn_coffeesql+nc_coffeesql+sk_coffeesql+srng_coffeesql+zdn_coffeesql+zs_coffeesql+zds_coffeesql+
    ddo_coffeesql+do_coffeesql+ddn_coffeesql+dds_coffeesql+doc_coffeesql),total_cacaoaddr=len(adn_cacaosql+ads_cacaosql+sds_cacaosql+
    magui_cacaosql+ns_cacaosql+leyte_cacaosql+sleyte_cacaosql+mo_cacaosql+bukd_cacaosql+
    ldn_cacaosql+nc_cacaosql+sk_cacaosql+srng_cacaosql+zdn_cacaosql+zs_cacaosql+zds_cacaosql+
    ddo_cacaosql+do_cacaosql+ddn_cacaosql+dds_cacaosql+doc_cacaosql),total_coconutaddr=len(adn_coconutsql+ads_coconutsql+sds_coconutsql+
    magui_coconutsql+ns_coconutsql+leyte_coconutsql+sleyte_coconutsql+mo_coconutsql+bukd_coconutsql+
    ldn_coconutsql+nc_coconutsql+sk_coconutsql+srng_coconutsql+zdn_coconutsql+zs_coconutsql+zds_coconutsql+
    ddo_coconutsql+do_coconutsql+ddn_coconutsql+dds_coconutsql+doc_coconutsql),total_pfnaddr=len(adn_pfnsql+ads_pfnsql+sds_pfnsql+
    magui_pfnsql+ns_pfnsql+leyte_pfnsql+sleyte_pfnsql+mo_pfnsql+bukd_pfnsql+
    ldn_pfnsql+nc_pfnsql+sk_pfnsql+srng_pfnsql+zdn_pfnsql+zs_pfnsql+zds_pfnsql+
    ddo_pfnsql+do_pfnsql+ddn_pfnsql+dds_pfnsql+doc_pfnsql),datatable=datatable,maless=male_singlesolesql, femaless=female_singlesolesql)

@app.route("/menu")
def menu():
    if(is_on_session()):
        return render_template("menu.html")
    else:
        return redirect("/login?force_url=1")


@app.route("/cform")
def cform():
    return render_template("formc.html")


@app.route("/spreadsheet")
def spreadsheet():
    return render_template("spreadsheet.html")



@app.route("/resp_prof")
def resp_prof():
    return render_template("resp_prof.html")


@app.route("/bsns_info")
def bsns_info():
    return render_template("bsns_info.html")

@app.route("/ciboasn")
def ciboasn():
    return render_template("ciboasn.html")

@app.route("/dcf/dcf_trade_promotion")
def dcf_trade_promotion():
    return render_template("dcf_trade_promotion.html")


@app.route("/dcf/dcf_product_development")
def dcf_product_development():
    return render_template("dcf_product_development.html")

@app.route("/dcf/dcf_matching_grant")
def dcf_matching_grant():
    return render_template("dcf_matching_grant.html")

@app.route("/dcf/dcf_enablers_tracker")
def dcf_enablers_tracker():
    return render_template("dcf_enablers_tracker.html")

@app.route("/dcf/dcf_equity_tracker")
def dcf_equity_tracker():
    return render_template("dcf_equity_tracker.html")

@app.route("/dcf/dcf_dip_preparation_tracker")
def dcf_dip_preparation_tracker():
    return render_template("dcf_dip_preparation_tracker.html")

if __name__ == "__main__":
    app.run(debug=True)

    # sample edit