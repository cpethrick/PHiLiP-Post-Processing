import os;CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]+"/";
import sys
sys.path.append(CURRENT_PATH+"../../src");
from plot_unsteady_integrated_turbulent_flow_quantities import plot_periodic_turbulence
#-----------------------------------------------------
#=====================================================
# Input variables for plotting
#=====================================================
global subdirectories, filenames, labels, black_line_flag, \
dashed_line_flag, figure_filename_postfix, figure_title, \
ylimits_kinetic_energy_input, ylimits_dissipation_input, \
log_axes_input, legend_on_input, legend_inside_input, \
plot_reference_result, nlegendcols_input, \
figure_subdirectory, data_directory_base, figure_directory_base, \
smoothing_input, has_numerical_entropy, has_relaxation_parameter
#=====================================================
def plot_for_presentation(
    subdirectories_for_plot,
    labels_for_plot,
    black_line_flag_for_plot,
    dashed_line_flag_for_plot,
    has_numerical_entropy_for_plot,
    has_relaxation_parameter_for_plot,
    final_time_for_plot=10.0,
    legend_fontSize_input=14):
    global subdirectories, filenames, labels, black_line_flag, \
    dashed_line_flag, figure_filename_postfix, figure_title, \
    ylimits_kinetic_energy_input, ylimits_dissipation_input, \
    log_axes_input, legend_on_input, legend_inside_input, \
    plot_reference_result, nlegendcols_input, \
    figure_subdirectory, data_directory_base, figure_directory_base, \
    smoothing_input, has_numerical_entropy, has_relaxation_parameter
    #-----------------------------------------------------
    for i in range(0,len(subdirectories_for_plot)):
        figure_filename_postfix_input=figure_filename_postfix+"_%i" % i
        #-----------------------------------------------------
        subdirectories.append(subdirectories_for_plot[i])
        filenames.append("turbulent_quantities.txt")
        labels.append(labels_for_plot[i])
        black_line_flag.append(black_line_flag_for_plot[i])
        dashed_line_flag.append(dashed_line_flag_for_plot[i])
        has_numerical_entropy.append(has_numerical_entropy_for_plot[i])
        has_relaxation_parameter.append(has_relaxation_parameter_for_plot[i])
        #-----------------------------------------------------
        plot_periodic_turbulence(
            figure_subdirectory,
            subdirectories,
            filenames,
            labels,
            black_line_flag,
            dashed_line_flag,
            figure_directory_base,
            data_directory_base,
            False,
            figure_filename_postfix_input,
            figure_title,
            log_axes_input,
            legend_on_input,
            legend_inside_input,
            nlegendcols_input,
            has_numerical_entropy=has_numerical_entropy,
            has_relaxation_parameter=has_relaxation_parameter,
            # clr_input=clr_input,
            transparent_legend_input=True,
            tmax=final_time_for_plot,
            legend_fontSize_input=legend_fontSize_input,
            solid_and_dashed_lines=False,
            plot_kinetic_energy=True,
            plot_enstrophy=True,
            plot_numerical_dissipation=True,
            plot_PHiLiP_DNS_result_as_reference=True,
            dissipation_rate_smoothing=smoothing_input)
    #-----------------------------------------------------
#=====================================================
def reinit_inputs():
    global subdirectories, filenames, labels, black_line_flag, \
    dashed_line_flag, figure_filename_postfix, figure_title, \
    ylimits_kinetic_energy_input, ylimits_dissipation_input, \
    log_axes_input, legend_on_input, legend_inside_input, \
    plot_reference_result, nlegendcols_input, \
    figure_subdirectory, data_directory_base, figure_directory_base, \
    smoothing_input, has_numerical_entropy, has_relaxation_parameter

    subdirectories = []
    filenames = []
    labels = []
    black_line_flag = []
    dashed_line_flag = []
    figure_filename_postfix = "" # default
    figure_title = "" # default
    ylimits_kinetic_energy_input = [] # default
    ylimits_dissipation_input = [] # default
    log_axes_input=None # default
    legend_on_input=True # default
    legend_inside_input=False # default
    plot_reference_result=True # default
    nlegendcols_input=1
    figure_subdirectory="" # default
    data_directory_base = " "#"/Users/Julien/julien_phd/post_processing/data/taylor_green_vortex" # i think this is useless
    # figure_directory_base = "/Users/Julien/julien_phd/post_processing/figures/taylor_green_vortex"
    figure_directory_base = "figures"
    smoothing_input = []
    has_numerical_entropy = [] 
    has_relaxation_parameter = []
#=====================================================
#-----------------------------------------------------
#=====================================================
# DOFs: 96^3 | LRNC Advanced SGS Models on GL flux nodes (no filter width modifications)
#-----------------------------------------------------
if(True):
    reinit_inputs()
    data_directory_base="/home/carolyn/Documents/AIAA2024/central-viscous-flux"
    date_for_runs="."
    figure_subdirectory="2024_AIAA"
    figure_title = "TGV at Re$_{\\infty}=1600$, P$5$, $96^{3}$ DOFs, CFL$=0.10$" # comment to turn off
    figure_filename_postfix = "compare_FDSD"
    legend_inside_input=True
    #-----------------------------------------------------
    subdirectories_for_plot=[\
    "juliens_results/robustness/viscous_TGV_ILES_NSFR_cDG_IR_2PF_GL_OI-0_dofs024_p5_procs16",\
    "FD-24DOF",\
    "FD-24DOF-SIP",\
    "juliens_results/robustness/viscous_TGV_ILES_NSFR_cDG_IR_2PF_GL_OI-0_dofs048_p5_procs64/",\
    "FD-48DOF",\
    "FD-48DOF-SIP",\
    "juliens_results/viscous_TGV_ILES_NSFR_cPlus_IR_2PF_GL_OI-0_dofs096_p5_procs512",\
    "FD-96DOF",\
    #"juliens_results/time_step_advantage_with_physical_check/viscous_TGV_ILES_NSFR_cPlus_IR_2PF_GL_OI-0_dofs096_p5_CFL-0.36_procs512",\
    ]
    # labels
    labels_for_plot=[\
    "$24^{3}$ DOFs, $c_{DG}$ NSFR.IR-GL",\
    "FD, CV, $24^{3}$ DOFs, $c_{+}$ NSFR.Ra-GL",\
    "FD, SIP, $24^{3}$ DOFs, $c_{+}$ NSFR.Ra-GL",\
    "$48^{3}$ DOFs, $c_{DG}$ NSFR.IR-GL",\
    "FD, CV, $48^{3}$ DOFs, $c_{+}$ NSFR.Ra-GL",\
    "FD, SIP, $48^{3}$ DOFs, $c_{+}$ NSFR.Ra-GL",\
    "$96^{3}$ DOFs, $c_{+}$ NSFR.IR-GL",\
    "FD, CV, $48^{3}$ DOFs, $c_{+}$ NSFR.Ra-GL",\
    "$96^{3}$ DOFs, $c_{+}$ NSFR.IR-GL, CFL$=0.36$",\
    ]
    black_line_flag_for_plot=[\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    ]
    smoothing_input = [\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    False,\
    True,\
    False,\
    False,\
    False,\
    False,\
    ]
    has_numerical_entropy_for_plot=[\
    False,\
    True,\
    True,\
    False,\
    True,\
    True,\
    False,\
    True,\
    False,\
    ]
    # has_relaxation_parameter_for_plot=[\
    # False,\
    # True,\
    # True,\
    # False,\
    # True,\
    # True,\
    # False,\
    # True,\
    # False,\
    # ]
    has_relaxation_parameter_for_plot = has_numerical_entropy_for_plot
    dashed_line_flag_for_plot = [not a for a in  has_numerical_entropy_for_plot]
    plot_for_presentation(subdirectories_for_plot,labels_for_plot,black_line_flag_for_plot,dashed_line_flag_for_plot,has_numerical_entropy_for_plot,has_relaxation_parameter_for_plot,legend_fontSize_input=12)
