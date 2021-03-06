import shutil

from S_replace_variables import replace_variables
from S_brute_force import brute_force
from S_multipolyfit import getBest
from S_polyclean_file import polyfit


from S_get_inverse import get_inverse
from S_get_log import get_log
from S_get_exp import get_exp
from S_get_sin import get_sin
from S_get_asin import get_asin
from S_get_cos import get_cos
from S_get_acos import get_acos
from S_get_tan import get_tan
from S_get_atan import get_atan
from S_get_squared import get_squared
from S_get_sqrt import get_sqrt

def try_bf_polyfit(pathdir, filename, methods_tried, BF_try_time, BF_ops_file_type, BF_sep_type, use_MDL, check_prefactor, dim_red_file, maxdeg_polyfit, err_threshold_polyfit, first_run, move_dir, original_dir, solved_dir, BF_transf_name, poly_transf_name):
    if first_run:
        # Try brute force                                                                                                                                                    
        
        BF_formula, methods_tried  = brute_force(pathdir,filename,methods_tried,BF_transf_name,BF_try_time,BF_ops_file_type,2,use_MDL, check_prefactor)
        if BF_formula!= 0:
            not_replaced_BF_formula = BF_formula
            BF_formula = replace_variables(dim_red_file,filename.split('-')[0],BF_formula)
            if move_dir!=0:
                shutil.move(original_dir+filename.split('-')[0], solved_dir)
            return (BF_formula, methods_tried, not_replaced_BF_formula)
        
        BF_formula, methods_tried = brute_force(pathdir,filename,methods_tried,BF_transf_name,BF_try_time,BF_ops_file_type,3,use_MDL, check_prefactor)
        if BF_formula!= 0:
            not_replaced_BF_formula = BF_formula
            BF_formula = replace_variables(dim_red_file,filename.split('-')[0],BF_formula)
            if move_dir!=0:
                shutil.move(original_dir+filename.split('-')[0], solved_dir)
            return (BF_formula, methods_tried, not_replaced_BF_formula)
        
    else:
        BF_formula, methods_tried  = brute_force(pathdir,filename,methods_tried,BF_transf_name,BF_try_time,BF_ops_file_type,BF_sep_type,use_MDL, check_prefactor)
        if BF_formula!= 0:
            not_replaced_BF_formula = BF_formula
            BF_formula = replace_variables(dim_red_file,filename.split('-')[0],BF_formula)
            if move_dir!=0:
                shutil.move(original_dir+filename.split('-')[0], solved_dir)
            return (BF_formula, methods_tried, not_replaced_BF_formula)


    # Try polyfit                                                                                                                                                      
    methods_tried = methods_tried + [poly_transf_name]
    poly_solved, obtained_eq = polyfit(maxdeg_polyfit,pathdir+filename,err_threshold_polyfit)
    if poly_solved==1:
        methods_tried = methods_tried + ["solved"]
        obtained_eq = replace_variables(dim_red_file,filename.split('-')[0],obtained_eq)
        if move_dir!=0:
            shutil.move(original_dir+filename.split('-')[0], solved_dir)
        return (obtained_eq, methods_tried, obtained_eq)


    return (0,methods_tried,0)
