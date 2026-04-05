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
<meta name="ncbi_phid" content="0C424B4B9D0DBCD10000000000000001">
<meta name="ncbi_sessionid" content="0C424B4B9D0DBCD1_0000SID">

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
<td align="right">Not logged in | <a href="/geo/submitter?ix=1NmPL5_b5FeKJev7IbDJRu3Z21DAMXERp1_Hfv4rec52jA5ug7cPSSpcOIdcys01wHHOa6d5StZ84n1ZLo7w3w">Login</a><a href="javascript:RPopUpWindow_Set(geologinbar_login,260,200,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
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
&nbsp;<label for="geo_acc">GEO accession: </label><input id="geo_acc" name="acc" onkeydown="ViewOptionsFormKeyDown(event)" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_acc)" style="font-size: 10px" type="text" value="GSM8722494">&nbsp;&nbsp;</td>
<td valign="middle"><img alt="Go" border="0" onclick="SubmitViewOptionsForm()" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_go)" src="/geo/img/buttons/go_button.gif"></td>
</tr></table></td></tr></table></td>
</tr></table></form>
    <table><tr><td><table cellpadding="2" cellspacing="0" width="600"><tr bgcolor="#cccccc" valign="top"><td colspan="2"><table width="600"><tr><td><strong class="acc" id="GSM8722494"><a href="/geo/query/acc.cgi?acc=GSM8722494" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">Sample GSM8722494</a></strong></td>
<td></td>
<td align="right" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_gds)"><a href="/gds/?term=GSM8722494[Accession]">Query DataSets for GSM8722494</a></td>
</tr></table></td></tr>
<tr valign="top"><td>Status</td>
<td>Public on May 07, 2025</td>
</tr>
<tr valign="top"><td nowrap>Title</td>
<td style="text-align: justify">Multiplexed scRNA-seq from Gastruloids of various size at 144h rep1</td>
</tr>
<tr valign="top"><td nowrap>Sample type</td>
<td>SRA</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Source name</td>
<td style="text-align: justify">Gastruloids<br></td>
</tr>
<tr valign="top"><td nowrap>Organism</td>
<td><a href="/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=10090" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_organismus)">Mus musculus</a></td>
</tr>
<tr valign="top"><td nowrap>Characteristics</td>
<td style="text-align: justify">tissue: Gastruloids<br>Stage: 144h<br>multiplexing: CellPlex<br>background: 129/SVEV<br>library type: GEX<br></td>
</tr>
<tr valign="top"><td nowrap>Extracted molecule</td>
<td>polyA RNA</td>
</tr>
<tr valign="top"><td nowrap>Extraction protocol</td>
<td style="text-align: justify">Gastruloids seeded from different cell numbers (100, 300, 600, 1800, 5400 cells) were grown until 120 h and 144 h across two independent replicates. For each condition the number of gastruloids used was chosen to unsure that a minimum of 200 000 cells were obtained for each sample and a minimum of 24 gastruloids were collected for each sample to limit the impact of gastruloids-to-gastruloids variation. Gastruloids were collected and washed in 1ml of PBS in a 1.7 ml Eppendorf tube and dissociated using 100μl of Accutase (Stempro) for 5 minutes at 37°C. Full dissociation was verified to ensure absence of doublets and if necessary, it was completed using mechanical dissociation by pipetting. All centrifugation were done at 400 g for 5 minutes. Conditions were multiplex using the CellPlex procedure according to manufacturer’s recommendations. Cells were incubated in 50μl of cell multiplexing oligos (3’ CellPlex Kit Set A, PN-1000261) for 5 minutes at room temperature. They were then thoroughly washed three times with 1 ml PBS 1% BSA ensuring to remove as much as possible of the supernatant each time to prevent sample-to-sample contamination. Each sample was then counted and viability was assessed using a Countess 3 automated cell counter (Invitrogen) and viability was above 90% in all cases. Samples were then pooled in desired proportion to ensure proper representation of each experimental condition and the pooled cell suspension was filtered using a 40 μm cell strainer (Flowmi, BAH136800040). The final count was performed and 24 000 cells were targeted for recovery using the 10x Genomics approach following their recommendations since multiplexing allows for the resolution of more doublet cells, yielding on average 15000 singlet cells that can be used for analysis.<br>The pool of cells was counted and subjected to single cell RNA-seq following manufacturer’s recommendation (protocol CG000388 Rev A). We aimed for a recovery of c.a. 24000 cells per sample as a large number of  doublet droplets can be resolved with this method. cDNA preparations were performed according to 10x Genomics recommendations, amplified for 10–12 cycles and verified on fragment analyser. Both cell multiplexing oligo, and gene expression libraries were sequenced on a Novaseq (Illumina protocol #1000000106351 v03) with the cbot2 chemistry.<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Library strategy</td>
<td>RNA-Seq</td>
</tr>
<tr valign="top"><td nowrap>Library source</td>
<td>transcriptomic single cell</td>
</tr>
<tr valign="top"><td nowrap>Library selection</td>
<td>cDNA</td>
</tr>
<tr valign="top"><td nowrap>Instrument model</td>
<td>Illumina NovaSeq 6000</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Description</td>
<td style="text-align: justify">Library name: 144h_size_rep1_GEX<br></td>
</tr>
<tr valign="top"><td nowrap>Data processing</td>
<td style="text-align: justify">Single-cell analysis was performed as previously described (Mayran et al. 2023). Fastq files containing the sample information (cell multiplexing oligo) were processed with CITE-seq-Count version 1.4.4 using the following arguments: --cell_barcode_first_base 1 --cell_barcode_last_base 16 --umi_first_base 17 --umi_last_base 28 --expected_cells 24000 --whitelist ’cellranger_barcodes_3M-february-2018.txt’ The barcodes were then translated (8th and 9th base were changed to their complementary bases) to match the barcode cells of the Gene Expression part. The reads containing the expression part were processed with STARSolo version 2.7.10b using: --sjdbOverhang 100 --sjdbGTFfile ’input.gtf’ --soloType CB_UMI_Simple --soloCBwhitelist ’cellranger_barcodes_3M-february-2018.txt’ --soloUMIlen 12 --soloUMIdedup 1MM_CR --soloUMIfiltering - --soloCellFilter None --outSAMmapqUnique 60 The GTF file is available at <a href="https://zenodo.org/records/10079673.">https://zenodo.org/records/10079673.</a> Barcodes associated with empty droplets were filtered with DropletUtils using the EmptyDrops method with a lower-bound threshold of 100 and a false discovery rate (FDR) threshold of 0.01. Matrices were then processed with Seurat version 4.3.0 in R version 4.3.0, following the methods described in Mayran et al. (2023). Barcodes with fewer than 200 identified genes and genes detected in fewer than three cells were filtered out. For CMO libraries, demultiplexing was performed in R using counts from CITE-seq-Counts. Cell barcodes with fewer than 5 CMO UMIs or absent in the Seurat object were discarded. Sample attribution was performed using demuxmix with the total number of UMIs per cell. Cells classified as non-singlets (negative, unsure, or doublets) were excluded. Low-quality cells and potential doublets were removed based on the mean UMI content and mitochondrial percentage. Barcodes with fewer than 0.4 times or more than 2.5 times the mean UMI, and those outside of 0.05% to 8% mitochondrial UMIs, were excluded. The matrices were normalized, and the cell cycle score (using the 2019 updated gene list from Seurat) was computed. Samples were merged using the merge command in Seurat. The combined object was normalized, 2000 variable features were identified, and the data was scaled and regressed by cell cycle score and mitochondrial percentage. Principal components were computed using variable genes within the 5th and 80th percentiles of expression to limit batch effects. UMAP and k-nearest neighbors were computed with 25 principal components, and the clustering resolution (0.6) was optimized to avoid duplicate or missing clusters. Cluster annotation was performed manually using marker genes. Genes from the module analysis of the BRB-seq experiment were scaled across the dataset and split to display each seeding number in Fig. 4E. The list of genes within each module was scored using the addModuleScore command in Seurat, and a custom featurePlot visualization was used as described in Mayran et al. 2023.<br>Assembly: mm10<br>Supplementary files format and content: metadata.csv: a comma separated table where each row is a cell and columns are metadata associated to each cell as well as the coordinates on the UMAP.<br>Supplementary files format and content: tar.gz: output of STARsolo or CITE-seq-Counts (translated) as output of cellranger (genes.tsv, barcodes.tsv, matrix.mtx)<br>Supplementary files format and content: RDS: R object with everything to redo the plots<br>Supplementary files format and content: CMO.Samples.csv.gz: comma separated text file with for each Library (first column), the different samples (second column), with their barcodes (third column).<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Submission date</td>
<td>Jan 09, 2025</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Last update date</td>
<td>May 07, 2025</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Contact name</td>
<td>ALEXANDRE MAYRAN</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>E-mail(s)</td>
<td><a href="mailto:alexandre.mayran@epfl.ch">alexandre.mayran@epfl.ch</a><br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Organization name</td>
<td style="text-align: justify">EPFL<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Street address</td>
<td style="text-align: justify">Station 19<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>City</td>
<td style="text-align: justify">LAUSANNE</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>State/province</td>
<td style="text-align: justify">Waadt</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>ZIP/Postal code</td>
<td style="text-align: justify">1015</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Country</td>
<td style="text-align: justify">Switzerland</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td>Platform ID</td>
<td><a href="/geo/query/acc.cgi?acc=GPL24247">GPL24247</a></td>
</tr>
<tr valign="top"><td>Series (2)</td>
<td onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSE286273" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSE286273</a></td>
<td valign="top">Size-dependent temporal decoupling of morphogenesis and transcriptional programs in pseudo-embryos [scRNA-seq]</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSE286428" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSE286428</a></td>
<td valign="top">Size-dependent temporal decoupling of morphogenesis and transcriptional programs in pseudo-embryos</td>
</tr>
</table></td>
</tr>
<tr valign="top"><td colspan="2"><strong>Relations</strong></td></tr>
<tr valign="top"><td>BioSample</td>
<td><a href="https://www.ncbi.nlm.nih.gov/biosample/SAMN46181701">SAMN46181701</a></td>
</tr>
<tr valign="top"><td>SRA</td>
<td><a href="https://www.ncbi.nlm.nih.gov/sra?term=SRX27299527">SRX27299527</a></td>
</tr>
</table>
<br><span id="gdv"></span><table cellpadding="2" cellspacing="2" width="600"><tr bgcolor="#eeeeee" valign="top"><td align="middle" bgcolor="#CCCCCC"><strong>Supplementary file</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Size</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Download</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>File type/resource</strong></td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSM8722494_144h_size_rep1_GEX.tar.gz</td>
<td bgcolor="#DEEBDC" title="181218439">172.8 Mb</td>
<td bgcolor="#DEEBDC"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8722nnn/GSM8722494/suppl/GSM8722494%5F144h%5Fsize%5Frep1%5FGEX%2Etar%2Egz">(ftp)</a><a href="/geo/download/?acc=GSM8722494&amp;format=file&amp;file=GSM8722494%5F144h%5Fsize%5Frep1%5FGEX%2Etar%2Egz">(http)</a></td>
<td bgcolor="#DEEBDC">TAR</td>
</tr>
<tr><td><a href="/Traces/study/?acc=SRX27299527">SRA Run Selector</a><a href="javascript:RPopUpWindow_Set(geoaxema_srarun,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td></tr>
<tr><td class="message">Raw data are available in SRA</td></tr>
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


