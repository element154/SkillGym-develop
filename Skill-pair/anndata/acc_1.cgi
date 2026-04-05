<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
  <HEAD>
    
    <style type="text/css">
      a { text-decoration: none; }
	.bordergc {background-color: #6699CC;}
	.bordergd {background-color: #B6C7E5;}
	.borderge {background-color: #EEF3FB;}
	.bordergf {background-color: #FFFFFF;}
	.bordergg {background-color: #CCCCCC;}
      .small8b { font-size:8pt;
                font-family: ariel,helvetica,sans-serif;
                color:#6633cc;
              }
      .small8db { font-size:8pt;
                font-family: ariel,helvetica,sans-serif;
                color:#4411aa;
              }

    </style>
    <META http-equiv="Content-Type"
      content="text/html; charset=UTF-8">
    <META name="keywords"
      CONTENT="NCBI GEO Gene Expression Omnibus microarray oligonucleotide array SAGE">
    <META name="description"
      content="NCBI's Gene Expression Omnibus (GEO) is a public archive and resource for gene expression data.">

<meta name="ncbi_app" content="geo">
<meta name="ncbi_pdid" content="full">
<meta name="ncbi_phid" content="0751BE0A9D0DB8910000000000000001">
<meta name="ncbi_sessionid" content="0751BE0A9D0DB891_0000SID">

    <TITLE>
    GEO Accession viewer
    </TITLE>
    <link rel="stylesheet"
      href="/corehtml/ncbi.css">
    <!-- GEO_SCRIPT -->

<SCRIPT LANGUAGE="JavaScript1.2"
SRC="/coreweb/javascript/imagemouseover.js"></SCRIPT>

<SCRIPT LANGUAGE="JavaScript1.2"
SRC="/coreweb/javascript/show_message.js"></SCRIPT>

<script type="text/javascript" src="/corehtml/jsutils/utils.1.js"></script>

<script type="text/javascript" src="/corehtml/jsutils/remote_data_provider.1.js"></script>

<SCRIPT LANGUAGE="JavaScript1.2"
SRC="/geo/js/help_def_messages.js"></SCRIPT>

<script type="text/javascript">
    window.onload = function () {
        jQuery.getScript("/core/alerts/alerts.js", function () {
            galert(['#galerts_table','body > *:nth-child(1)'])
        });
    }
</script>



<LINK  rel = STYLESHEET href = "../info/geo_style.css" Type  = "text/css" >
<link rel="stylesheet" type="text/css" href="acc.css" />
  <script language="Javascript">

  function OnFormFieldChange()
  {
    var view = document.getElementById("view");

    if(document.getElementById("ViewOptions").form.value == 'html')
    {
        view.remove(3);
        view.remove(2);
    }
    else
    {
        var NewOption = document.createElement("OPTION");

        NewOption.text = "Full";
        NewOption.value = "full";

        try
        {
            view.add(NewOption, null);
        }
        catch(ex)
        {
            view.add(NewOption);
        }

        NewOption = document.createElement("OPTION");

        NewOption.text = "Data";
        NewOption.value = "data";

        try
        {
            view.add(NewOption, null);
        }
        catch(ex)
        {
            view.add(NewOption);
        }
    }
  }

  function SubmitViewOptionsForm()
  {
	var form = document.forms.ViewOptions;
    if(form.form.value == 'html')
    {
		form.form.setAttribute('disabled','disabled');
		if (form.view.value == 'quick') {
			form.view.setAttribute('disabled','disabled');
		}
		if (form.targ.value == 'self') {
			form.targ.setAttribute('disabled','disabled');
		}
        var token = document.getElementById("token_input");
        if (token) {
            form.token.value = token.value;
        } else {
            form.token.setAttribute('disabled','disabled');
        }
        form.submit();
    }
    else
    {
        window.open("acc.cgi?acc=" + form.acc.value + "&targ=" + form.targ.value +
                  "&form=" + form.form.value + "&view=" + form.view.value, "_self");
    }

    return false;
  }
  
  function ViewOptionsFormKeyDown(event)
  {
	if (event == undefined)
	{    
		event = window.event;
	}
	if (event.keyCode == 13)
	{
		SubmitViewOptionsForm();
		return false;
	}
  };

  function OpenFTP(url)
  {
    window.open(url.replace('ftp://', 'https://'), '_blank');
  }

  function OpenLink(url, where)
  {
    window.open(url, where);
  }

  utils.addEvent(window, "load", OnFormFieldChange)
  </script>

</head>
<body background="/coreweb/template1/pix/bg_main3.gif" topmargin="20" marginheight="20">


<script type="text/javascript" src="/core/jig/1.15.10/js/jig.min.js"></script>
<script type="text/javascript" src="/corehtml/pmc/granthub/v1/granthubsearch.min.js"></script>
<script type="text/javascript" src="/geo/js/dd_menu.js"></script>
	<table width="740" border="0" cellspacing="0" cellpadding="0" align="center" >
			<tr>
				<td>
					<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
						<tr>
							<td><a href="/"><img src="/geo/img/ncbi_logo.gif" alt="NCBI Logo" width="145" height="66" border="0"></a></td>
							<td width="100%" align="center" valign="middle" nowrap background="/coreweb/template1/pix/top_bg_white.gif"><img src="/coreweb/template1/pix/pixel.gif" width="550" height="1" alt="" border="0"><br>
								<a href="/geo/"><img src="/geo/img/geo_main.gif" alt="GEO Logo" border="0"></a>
							</td>
							<td align="right" background="/coreweb/template1/pix/top_bg_white.gif"><img src="/coreweb/template1/pix/top_right.gif" alt="" width="5" height="66" border="0"></td>
						</tr>
					</table>
					<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
						<tr>
							<td><img src="/coreweb/template1/pix/top2_left.gif" width="601" height="2" alt="" border="0"></td>
							<td width="100%" background="/coreweb/template1/pix/top2_mid_bg.gif"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td>
							<td align="right"><img src="/coreweb/template1/pix/top2_right.gif" alt="" width="14" height="2" border="0"></td>
						</tr>
					</table>
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" id="galerts_table"/>
					<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
						<tr>
							<td><img src="/coreweb/template1/pix/top3_ulm_no_a.gif" width="145" height="16" alt="" border="0" usemap="#unlmenu" name="unl_menu_pix"></td>
							<td background="/coreweb/template1/pix/top3_mainmenu_mid_bg.gif"><img src="/coreweb/template1/pix/top3_mainmenu_left.gif" width="3" height="16" alt="" border="0"></td>
							<td width="100%" valign="middle" nowrap background="/coreweb/template1/pix/top3_mainmenu_mid_bg.gif">

					<!-- GEO Navigation -->
			<ul id="geo_nav_bar">
				<li><a href="#">GEO Publications</a>
					<ul class="sublist">
						<li><a href="/geo/info/GEOHandoutFinal.pdf">Handout</a></li>
                        <li><a href="/pmc/articles/PMC10767856/">NAR 2024 (latest)</a></li>
						<li><a href="/pmc/articles/PMC99122/">NAR 2002 (original)</a></li>
						<li><a href="/pmc/?term=10767856,4944384,3531084,3341798,3013736,2686538,2270403,1669752,1619900,1619899,539976,99122">All publications</a></li>
					</ul>
				</li>
				<li><a href="/geo/info/faq.html">FAQ</a></li>
				<li><a href="/geo/info/MIAME.html" title="Minimum Information About a Microarray Experiment">MIAME</a></li>
				<li><a href="mailto:geo@ncbi.nlm.nih.gov">Email GEO</a></li>
			</ul>
			<!-- END GEO Navigation -->

                    </td>
                    <td background="/coreweb/template1/pix/top3_mainmenu_mid_bg.gif" align="right"><img src="/coreweb/template1/pix/top3_mainmenu_right.gif" width="5" height="16" alt="" border="0"></td>
                </tr>
            </table>
            
            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr>
                    <td><img src="/coreweb/template1/pix/top4_ulm_left.gif" width="145" height="4" alt="" border="0"></td>
                    <td width="100%" background="/coreweb/template1/pix/top4_mid_bg.gif"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td>
                    <td align="right" background="/coreweb/template1/pix/top4_mid_bg.gif"><img src="/coreweb/template1/pix/top4_ulm_right.gif" width="5" height="4" alt="" border="0"></td>
                </tr>
            </table>
    
            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr>
                    <td width=1 background="/coreweb/template1/pix/main_left_bg.gif"><img src="/coreweb/template1/pix/main_left_bg.gif" alt="" width="4" height="3" border="0"></td>
                    <td width="10000" bgcolor="#F0F8FF">
                        <table cellpadding="0" cellspacing="0" width="100%"><tr><td><font class="Top_Navigation_text" color="#2F6E87" face="Verdana" size="+1">&nbsp;&nbsp;&nbsp;<a href="/">NCBI</a> &gt; <a href="/geo"><font color="">GEO</font></a> &gt; <a href="acc.cgi"><b>Accession Display</b></a><a href="javascript:RPopUpWindow_Set(geologinbar_location,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></font></td>
<td align="right">Not logged in | <a href="/geo/submitter?ix=1vYKWGRZjr9tYUcft5bhEGJ2COVYIAMA-PEHYb_l99i-JIMKgGDG3OY9hpn95AawIIqFrqyAGNPhpwulKfQ94I">Login</a><a href="javascript:RPopUpWindow_Set(geologinbar_login,260,200,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
</tr></table>
                    </td>
                    <td width=1 background="/coreweb/template1/pix/main_right_bg.gif"><img src="/coreweb/template1/pix/main_right_bg.gif" width="4" height="3" alt="" border="0"></td>
                </tr>
                <tr>
                    <td background="/coreweb/template1/pix/main_left_bg.gif"><img src="/coreweb/template1/pix/main_left_bg.gif" width="4" height="1" alt="" border="0"></td>
                    <td width="10000" bgcolor="#E0EEEE"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td>
                    <td align="right" background="/coreweb/template1/pix/main_right_bg.gif"><img src="/coreweb/template1/pix/main_right_bg.gif" alt="" width="4" height="1" border="0"></td>
                </tr>

                <tr>
                    <td background="/coreweb/template1/pix/main_left_bg.gif"><img src="/coreweb/template1/pix/main_left_bg.gif" width="4" height="3" alt="" border="0"></td>
                    <td width="100%" bgcolor="White">
                        <table width="98%" border="0" align="center">
                            <tr>
                                <td>
                                    <table border="0" cellspacing="0" cellpadding="0" align="right" width="100%">
                                        <tr>
                                            <td>

 <script type="text/javascript" src="acc.js"></script>
 <span id="msg_err" style="color:red"></span>
 <span id="msg_info" style="color:blue"></span>
<table cellpadding="0" cellspacing="0" style="border: 1px solid #C0F8FF"><tr><td><img alt=" " height="35" src="/coreweb/template1/pix/pixel.gif" width="1"></td>
<td bgcolor="#F0F8FF" width="100%"><font color="#0066CC" face="Arial" size="1"><div id="HelpMessage" style="font: 11px/11px arial, sans-serif"><strong>GEO help:</strong> Mouse over screen elements for information.</div></font></td>
</tr></table>
<form action="acc.cgi" enctype="application/x-www-form-urlencoded" id="ViewOptions" method="POST" name="ViewOptions" target="_self"><table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td></td>
<td bgcolor="#CCCCCC" nowrap valign="middle" width="100%"><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td nowrap><table border="0" cellpadding="0" cellspacing="0"><tr><td valign="middle"><input id="token" name="token" type="hidden" value=""><label for="scope">Scope: </label><select id="scope" name="targ" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_scope)" style="font-size: 10px"><option selected value="self">Self</option>
<option value="gpl">Platform</option>
<option value="gsm">Samples</option>
<option value="gse">Series</option>
<option value="all">Family</option>
</select>
&nbsp;&nbsp;<label for="form">Format: </label><select id="form" name="form" onchange="OnFormFieldChange()" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_format)" style="font-size: 10px"><option value="html">HTML</option>
<option value="text">SOFT</option>
<option value="xml">MINiML</option>
</select>
&nbsp;&nbsp;<label for="view">Amount: </label><select id="view" name="view" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_amount)" style="font-size: 10px"><option value="brief">Brief</option>
<option selected value="quick">Quick</option>
</select>
&nbsp;<label for="geo_acc">GEO accession: </label><input id="geo_acc" name="acc" onkeydown="ViewOptionsFormKeyDown(event)" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_acc)" style="font-size: 10px" type="text" value="GSM6048170">&nbsp;&nbsp;</td>
<td valign="middle"><img alt="Go" border="0" onclick="SubmitViewOptionsForm()" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_go)" src="/geo/img/buttons/go_button.gif"></td>
</tr></table></td></tr></table></td>
</tr></table></form>
    <table><tr><td><table cellpadding="2" cellspacing="0" width="600"><tr bgcolor="#cccccc" valign="top"><td colspan="2"><table width="600"><tr><td><strong class="acc" id="GSM6048170"><a href="/geo/query/acc.cgi?acc=GSM6048170" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">Sample GSM6048170</a></strong></td>
<td></td>
<td align="right" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_gds)"><a href="/gds/?term=GSM6048170[Accession]">Query DataSets for GSM6048170</a></td>
</tr></table></td></tr>
<tr valign="top"><td>Status</td>
<td>Public on Jul 07, 2022</td>
</tr>
<tr valign="top"><td nowrap>Title</td>
<td style="text-align: justify">P29 single cell TCR of pre-Tx HNSCC tumor</td>
</tr>
<tr valign="top"><td nowrap>Sample type</td>
<td>SRA</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Source name</td>
<td style="text-align: justify">HNSCC tumor<br></td>
</tr>
<tr valign="top"><td nowrap>Organism</td>
<td><a href="/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=9606" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_organismus)">Homo sapiens</a></td>
</tr>
<tr valign="top"><td nowrap>Characteristics</td>
<td style="text-align: justify">cell marker: TCR: ab chains<br>single cell or bulk: Single cell<br>state: Pre-Tx<br>patient diagnosis: Head and neck squamous cell Carcinoma (HNSCC)<br>molecule: T cell receptor<br></td>
</tr>
<tr valign="top"><td nowrap>Extracted molecule</td>
<td>total RNA</td>
</tr>
<tr valign="top"><td nowrap>Extraction protocol</td>
<td style="text-align: justify">Fresh tumor tissue was transferred to a 6 cm tissue culture dish in a small volume of DMEM media and cut into &lt;2 mm pieces with a razor blade. Tissue pieces were centrifuged (400 g for 5 minutes at 4°C for all centrifuge steps) and resuspended in 2-5 mL of a collagenase-containing enzymatic digestion solution (Miltenyi Human Tumor Dissociation Kit #30-095-929), based on the weight of collected tissue, according to manufacturer’s instructions. Biopsies were incubated at 37°C for 20-30 minutes with mixing using a 5-10 mL serological pipet and intermittent gentle vortexing at 2-5-minute intervals. The extent of tumor tissue dissociation was variable and likely dependent on extracellular matrix abundance. The resulting cell suspension was passed through a 70 um nylon mesh filter and washed with an additional 5-10 mL of RPMI media. Filtered tumor cell suspensions were centrifuged and resuspended in 3 mL ACK red blood cell lysis buffer (Gibco #A1049201) for 1 minute at RT, then immediately diluted with 10 mL of PBS (Life Technologies #10437028). Cells were pelleted and resuspended in Zombie NIR (Biolegend) viability dye solution (1:500 in PBS), followed by a 15 minute incubation at RT in the dark. Cells were counted with a hemocytometer, yielding on average 1.3x104 live cells/mg of tumor tissue. Up to 500,000 live cells were then resuspended in 100 uL of FACS wash buffer (FWB; PBS, 2% FBS, 1 mM EDTA) with the addition of the following antibodies: TruStain FcX (Biolegend 422302), CD3-PE/Dazzle (Biolegend 300450), CD45-Pacific Blue (Biolegend 304022), CD66b-PE/Cy7 (Biolegend 305116) and CD15-APC (Biolegend 301908). Cells were incubated on ice for 20 minutes, washed with 1 mL FWB, filtered through 40 um flow-cap strainers, and then resuspended in 500 uL FWB. Cells were sorted using a FACS Aria II or III instrument (BD Biosciences). For most samples, 12-15 x 103 live CD45+CD66b- mononuclear cells (MNC) cells were sorted into T cell media (RPMI + 10% FBS) and immediately transferred to ice. All scRNA-seq was performed using the 10x Genomics 5’ V1 assay and protocols (10x Genomics). CD45+ cells isolated as above were centrifuged and washed with PBS containing 0.05% RNase-free BSA (ThermoFisher Scientific #AM2616), leaving a volume of &lt;32 uL after the final wash. Up to 15,000 cells based on cell sorter count were loaded into a Single Cell Chip A channel, along with reverse transcriptase reagent mixture and 5’ gel beads according to the manufacturer’s protocol.<br>Libraries were prepared accordingn to 10X Genomics protocols for 5' barcoded GEX and V(D)J TCR (Version 1)<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Library strategy</td>
<td>RNA-Seq</td>
</tr>
<tr valign="top"><td nowrap>Library source</td>
<td>transcriptomic</td>
</tr>
<tr valign="top"><td nowrap>Library selection</td>
<td>cDNA</td>
</tr>
<tr valign="top"><td nowrap>Instrument model</td>
<td>Illumina HiSeq 4000</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Data processing</td>
<td style="text-align: justify">Raw PBMC scRNA-sequencing reads were demultiplexed and aligned to the human reference genome (GRCh38-2020-A from 10x Genomics) for each pooled library using Cell Ranger (v4.0.0). Each pooled library contained multiple patient samples and timepoints; cells from each sample were labelled with distinct Hashtag oligonucleotides (HTO, Cell Hashing). Sequencing files for Gene Expression (measure mRNA level of cells) and Antibody Capture (measure HTO levels of cells) were fed to the “cellranger count” function with the –libraries flag, and the sequences of all HTO used in the library were fed to this function with –feature-ref flag. This generated a digital gene expression matrix, which measured the number of unique molecular identifier (UMI) for each gene and each cell barcode.<br>The raw gene-by-barcode count matrix was then processed to filter potential empty drops using emptyDrops function from DropletUtils (v1.8.0, R package) (Lun et al., 2019) with the parameters of “lower = 500, ignore = 5”. We initially selected droplets as containing a cell if total UMI counts of this droplet exceed the 99th percentile of the top 10,000 barcodes divided by 10. Finally, only cells with FDR&lt;=0.01 were retained as real cells for the following analysis. The raw HTO-by-barcode matrix was subsequently filtered based on identified real cells.<br>The filtered HTO-by-barcode matrix for each pooled library was processed using GMM-demux to distinguish singlets from doublets or multiplets based on detection of HTOs with default parameters (Xin et al., 2020). Predicted singlets with a confidence score&gt;=0.8 were defined as true singlet cells. Cell barcodes were then classified and allocated to respective patient samples based on hashtag identities. After processing, the gene-by-barcode count matrix was refined based on these identified singlets and used for the following analyses.<br>Raw tumor scRNA-sequencing reads were demultiplexed to FASTQ files using Cell Ranger mkfastq (v3.0.0, 10x Genomics), and the Cumulus cellranger-workflow implementation of Cell Ranger count (v4.0.0) on Terra (<a href="https://terra.bio/">https://terra.bio/</a>) was used to align reads to the human reference genome (GRCh38-2020-A) and generate a raw counts matrix (Li et al., 2020). Cumulus was used to filter cells from the Cell Ranger raw counts matrix with fewer than 400 UMIs, 200 genes, or greater than 20% of UMIs mapped to mitochondrial genes.<br>To generate the single-cell V(D)J sequences and annotate each library, we aligned TCR FASTQ reads to human GRCh38 V(D)J reference (v4.0.0 from 10X Genomics, modified to remove TRDD segments) using “cellranger vdj” function from Cell Ranger (v4.0.0). The filtered contig annotations, which contained high-level annotations of each high-confident cellular contig, were further filtered by removing records with ‘raw_consensus_id’ as ‘none’. For blood single-cell V(D)J analysis, the identities of different patient samples in each pooled library were labelled based on demultiplexing of the gene expression matrix.<br>Assembly: GRCh38<br>Supplementary files format and content: Each scRNA sequenting sample contains a .h5 file including Gene Expression (tumor and PBMC) and Antibody Capture (PBMC) information. Single cell TCR sequencing data for each sample were saved in a csv file, which is generated by 'cellranger vdj' function and shows the detailed clonotype information. Bulk TCR sequencing data for each sample were provided by Adaptive Biotech and were saved in a tsv file. Hashtag files contain the sequence of each hashtag and the corresponding patient sample information.<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Submission date</td>
<td>Apr 18, 2022</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Last update date</td>
<td>Jul 07, 2022</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Contact name</td>
<td>Shengbao Suo</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Organization name</td>
<td style="text-align: justify">Dana-Farber Cancer Institute<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Street address</td>
<td style="text-align: justify">360 Longwood Ave<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>City</td>
<td style="text-align: justify">Boston</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>State/province</td>
<td style="text-align: justify">MA</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>ZIP/Postal code</td>
<td style="text-align: justify">02215</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Country</td>
<td style="text-align: justify">USA</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td>Platform ID</td>
<td><a href="/geo/query/acc.cgi?acc=GPL20301">GPL20301</a></td>
</tr>
<tr valign="top"><td>Series (1)</td>
<td onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSE200996" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSE200996</a></td>
<td valign="top">Tissue-resident Memory and Circulating T cells are Early Responders to Pre-surgical Cancer Immunotherapy</td>
</tr></table></td>
</tr>
</table>
<br><span id="gdv"></span><table cellpadding="2" cellspacing="2" width="600"><tr bgcolor="#eeeeee" valign="top"><td align="middle" bgcolor="#CCCCCC"><strong>Supplementary file</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Size</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Download</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>File type/resource</strong></td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSM6048170_filtered_contig_annotations_P29_pre-Tx_TCR_sc_tumor.csv.gz</td>
<td bgcolor="#DEEBDC" title="185778">181.4 Kb</td>
<td bgcolor="#DEEBDC"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6048nnn/GSM6048170/suppl/GSM6048170%5Ffiltered%5Fcontig%5Fannotations%5FP29%5Fpre%2DTx%5FTCR%5Fsc%5Ftumor%2Ecsv%2Egz">(ftp)</a><a href="/geo/download/?acc=GSM6048170&amp;format=file&amp;file=GSM6048170%5Ffiltered%5Fcontig%5Fannotations%5FP29%5Fpre%2DTx%5FTCR%5Fsc%5Ftumor%2Ecsv%2Egz">(http)</a></td>
<td bgcolor="#DEEBDC">CSV</td>
</tr>
<tr><td class="message">Raw data not provided for this record</td></tr>
<tr><td class="message">Processed data provided as supplementary file</td></tr>
</table>
<span id="customDlArea"></span><br></td></tr></table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
        <td background="/coreweb/template1/pix/main_right_bg.gif"><img src="/coreweb/template1/pix/main_right_bg.gif" width="4" height="3" alt="" border="0"></td>
    </tr>
    <tr>
        <td background="/coreweb/template1/pix/but_left.gif"><img src="/coreweb/template1/pix/but_left.gif" width="4" height="4" alt="" border="0"></td>
        <td width="10000" bgcolor="#FFFFFF" background="/coreweb/template1/pix/but_mid_bg.gif"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td>
        <td align="right" background="/coreweb/template1/pix/but_right.gif"><img src="/coreweb/template1/pix/but_right.gif" alt="" width="4" height="4" border="0"></td>
    </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
	<tr>
        <td width="99%"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td><td valign="top" align="right"  nowrap>
	        <span class="HELPBAR">|<A HREF="https://www.nlm.nih.gov"> NLM </A>|<A HREF="https://www.nih.gov" CLASS="HELPBAR"> NIH </A>|<A HREF="mailto:geo@ncbi.nlm.nih.gov" CLASS="HELPBAR"> GEO Help </A>|<A HREF="/geo/info/disclaimer.html" CLASS="HELPBAR"> Disclaimer </A>|<a href="https://www.nlm.nih.gov/accessibility.html" class="HELPBAR"> Accessibility </a>|</span><br>
        </td>
	</tr>
</table>


<map name="unlmenu">
<area alt="NCBI Home" coords="2,0,39,15" href="/" onMouseOver="changpics(unl_menu_pix, unl_menu_home_a)" onMouseOut="changpics(unl_menu_pix, unl_menu_noa)">
<area alt="NCBI Search" coords="40,0,91,15" href="/ncbisearch/" onMouseOver="changpics(unl_menu_pix, unl_menu_search_a)" onMouseOut="changpics(unl_menu_pix, unl_menu_noa)">
<area alt="NCBI SiteMap" coords="92,0,143,15" href="/Sitemap/" onMouseOver="changpics(unl_menu_pix, unl_menu_sitemap_a)" onMouseOut="changpics(unl_menu_pix, unl_menu_noa)">
</map>

<script type="text/javascript" 
  src="/portal/portal3rc.fcgi/rlib/js/InstrumentNCBIBaseJS/InstrumentPageStarterJS.js"> </script>
</body>
</html>


