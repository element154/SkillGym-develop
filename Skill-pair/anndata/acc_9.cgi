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
<meta name="ncbi_phid" content="07513D5F9D0DBF610000000000000001">
<meta name="ncbi_sessionid" content="07513D5F9D0DBF61_0000SID">

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
<td align="right">Not logged in | <a href="/geo/submitter?ix=18u6bdBvpmV7_X_K47MIqc5n7dvonopYCceHqg9pv6cVTvHmZhg4pgu-DXs9IRC1PXsiPgy5Za86Oyj4FETEHI">Login</a><a href="javascript:RPopUpWindow_Set(geologinbar_login,260,200,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
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
&nbsp;<label for="geo_acc">GEO accession: </label><input id="geo_acc" name="acc" onkeydown="ViewOptionsFormKeyDown(event)" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_acc)" style="font-size: 10px" type="text" value="GSM8243014">&nbsp;&nbsp;</td>
<td valign="middle"><img alt="Go" border="0" onclick="SubmitViewOptionsForm()" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_go)" src="/geo/img/buttons/go_button.gif"></td>
</tr></table></td></tr></table></td>
</tr></table></form>
    <table><tr><td><table cellpadding="2" cellspacing="0" width="600"><tr bgcolor="#cccccc" valign="top"><td colspan="2"><table width="600"><tr><td><strong class="acc" id="GSM8243014"><a href="/geo/query/acc.cgi?acc=GSM8243014" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">Sample GSM8243014</a></strong></td>
<td></td>
<td align="right" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_gds)"><a href="/gds/?term=GSM8243014[Accession]">Query DataSets for GSM8243014</a></td>
</tr></table></td></tr>
<tr valign="top"><td>Status</td>
<td>Public on Nov 14, 2024</td>
</tr>
<tr valign="top"><td nowrap>Title</td>
<td style="text-align: justify">Kidney, Visium, Rep. 4</td>
</tr>
<tr valign="top"><td nowrap>Sample type</td>
<td>SRA</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Source name</td>
<td style="text-align: justify">Kidney<br></td>
</tr>
<tr valign="top"><td nowrap>Organism</td>
<td><a href="/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=10090" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_organismus)">Mus musculus</a></td>
</tr>
<tr valign="top"><td nowrap>Characteristics</td>
<td style="text-align: justify">tissue: Kidney<br>age: 6 weeks<br>strain: C57BL/6J<br>st method: Visium<br>Sex: Female<br></td>
</tr>
<tr valign="top"><td nowrap>Extracted molecule</td>
<td>polyA RNA</td>
</tr>
<tr valign="top"><td nowrap>Extraction protocol</td>
<td style="text-align: justify">10 µm fresh-frozen, OCT-embedded tissue sections on Array-seq slides were thawed at 37°C for 1 minute and fixed for 30-45 minutes at -20°C in 100% methanol. Following fixation, slides were dried for 1 minute at room temperature, and incubated with 2 U/µL Ribolock in 5X SSC for 5 minutes at room temperature. The SSC buffer was removed from the slide surface, sections were stained for 3 minutes at room temperature with hematoxylin, washed in nuclease-free water, and stained for 1 minute at room temperature with eosin diluted 1:10 in 0.45 M Tris-Acetic acid buffer, pH = 6.0. The slide was washed in nuclease-free water and kept at room temperature until dry and imaged at 20X magnification using an Olympus VS2000 slide scanner. Tissue sections were then permeabilized with 0.1% pepsin in 0.1 M HCl at 37°C for 15-20 minutes. After permeabilization, sections were washed once with 0.1X saline-sodium citrate (SSC) buffer. Tissue sections then underwent reverse transcription, tissue removal, exonuclease I treatment. cDNAs were eluted from the array by incubating for 10 minutes at room temperature in 0.1 M KOH and neutralized by adding 0.2X volume of 1M Tris-HCl.<br>cDNAs were purified using a DNA Clean &amp; Concentrator-5 kit and amplified using single-primer PCR using the KAPA HiFi HotStart ReadyMix kit. Amplified cDNAs were cleaned up using magnetic SPRISelect beads. 100 ng of amplified cDNA was tagmented using Tagment DNA TDE1 Enzyme and buffer for 5 min at 55°C and amplified by PCR using the Illumina Read1 primer and Illumina Read2-i7 reverse primers. Libraries were cleaned up using SPRISelect beads followed by gel purification using 2% E-Gel EX Agarose Gels and MinElute columns and quantified with the Qubit dsDNA High Sensitivity Assay Kit. Resulting libraries were sequenced on Illumina sequencing platforms.<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Library strategy</td>
<td>OTHER</td>
</tr>
<tr valign="top"><td nowrap>Library source</td>
<td>transcriptomic</td>
</tr>
<tr valign="top"><td nowrap>Library selection</td>
<td>other</td>
</tr>
<tr valign="top"><td nowrap>Instrument model</td>
<td>NextSeq 2000</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Data processing</td>
<td style="text-align: justify">Raw data processing: Fastq files from Array-seq and Visium sequencing experiments were generated using BaseSpace DRAGEN Analysis v1.3.0. To generate spatial count matrices, fastq files were processed using STARsolo from the STAR package version 2.7.10a with the mm10 mouse or CRCh38 human reference genome.  Array-seq data alignment and filtering: A custom python script was used to join STARsolo output count matrices and spot coordinates and generate a png image of points matching the x, y positions of each barcoded spot, colored based on UMI counts. The digitally generated Array-seq spot image is manually aligned with the H&amp;E image of the same section using Illustrator. A custom python script is used to detect tissue in the H&amp;E image and filter Array-seq data spots not under tissue.  VIsium data alignment: Visium datasets were filtered for spots under tissue and aligned to H&amp;E images by joining the tissue positions list csv, generated by the Spaceranger v1.2.0 software to the AnnData object generated from the STARSolo count matrix.  Clustering and differential expression: For spatial gene expression analysis using Scanpy, resulting count matrices were further filtered to keep (1) genes with at least 20 UMIs across all spots, and (2) spots with more than 120 UMIs in total. For clustering, data was normalized, log10 transformed, and clustered using principal component analysis (PCA), k-nearest neighbors (k-NN) identification, and the Leiden clustering algorithm. For differential expression analysis, we used the tl.rank_genes_groups() function in Scanpy. To map tissue subregions to spatial cluster obtained with the Leiden algorithm, we used the top 15 differentially expressed genes from each cluster for manual annotation. For plotting, spatial count or cluster identity were overlaid on the greyscale H&amp;E image using the Seaborn package.<br>Assembly: mm10 mouse or CRCh38 human reference genome<br>Supplementary files format and content: Raw count matrix data from STARSolo: Barcodes.tsv.gz, Features.tsv.gz, and matrix.mtx.gz<br>Supplementary files format and content: H5ad files contain raw count matricies with spot annotation of tissue subregion and scaled x,y coordinates.<br>Supplementary files format and content: Png files of each tissue H&amp;E section. Spot coordinates align to pixel coordinates of corresponding H&amp;E image files.<br>Library strategy: Spatial Transcriptomics<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Submission date</td>
<td>Apr 30, 2024</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Last update date</td>
<td>Nov 14, 2024</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Contact name</td>
<td>Denis Cipurko</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>E-mail(s)</td>
<td><a href="mailto:dcipurko@uchicago.edu">dcipurko@uchicago.edu</a><br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Phone</td>
<td style="text-align: justify">8472081507<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Organization name</td>
<td style="text-align: justify">University of Chicago<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Department</td>
<td style="text-align: justify">Biological Sciences Division<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Lab</td>
<td style="text-align: justify">Chevrier Lab<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Street address</td>
<td style="text-align: justify">900 E 57th St<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>City</td>
<td style="text-align: justify">Chicago</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>State/province</td>
<td style="text-align: justify">IL</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>ZIP/Postal code</td>
<td style="text-align: justify">60637</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Country</td>
<td style="text-align: justify">USA</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td>Platform ID</td>
<td><a href="/geo/query/acc.cgi?acc=GPL30172">GPL30172</a></td>
</tr>
<tr valign="top"><td>Series (1)</td>
<td onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSE266244" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSE266244</a></td>
<td valign="top">Repurposing Large-Format Microarrays for Scalable Spatial Transcriptomics</td>
</tr></table></td>
</tr>
<tr valign="top"><td colspan="2"><strong>Relations</strong></td></tr>
<tr valign="top"><td>BioSample</td>
<td><a href="https://www.ncbi.nlm.nih.gov/biosample/SAMN41141303">SAMN41141303</a></td>
</tr>
<tr valign="top"><td>SRA</td>
<td><a href="https://www.ncbi.nlm.nih.gov/sra?term=SRX24413938">SRX24413938</a></td>
</tr>
</table>
<br><span id="gdv"></span><table cellpadding="2" cellspacing="2" width="600"><tr bgcolor="#eeeeee" valign="top"><td align="middle" bgcolor="#CCCCCC"><strong>Supplementary file</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Size</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Download</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>File type/resource</strong></td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSM8243014_Visium_KI_4.png.gz</td>
<td bgcolor="#DEEBDC" title="17098558">16.3 Mb</td>
<td bgcolor="#DEEBDC"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8243nnn/GSM8243014/suppl/GSM8243014%5FVisium%5FKI%5F4%2Epng%2Egz">(ftp)</a><a href="/geo/download/?acc=GSM8243014&amp;format=file&amp;file=GSM8243014%5FVisium%5FKI%5F4%2Epng%2Egz">(http)</a></td>
<td bgcolor="#DEEBDC">PNG</td>
</tr>
<tr valign="top"><td bgcolor="#EEEEEE">GSM8243014_Visium_KI_4_annotated.h5ad</td>
<td bgcolor="#EEEEEE" title="158517960">151.2 Mb</td>
<td bgcolor="#EEEEEE"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8243nnn/GSM8243014/suppl/GSM8243014%5FVisium%5FKI%5F4%5Fannotated%2Eh5ad">(ftp)</a><a href="/geo/download/?acc=GSM8243014&amp;format=file&amp;file=GSM8243014%5FVisium%5FKI%5F4%5Fannotated%2Eh5ad">(http)</a></td>
<td bgcolor="#EEEEEE">H5AD</td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSM8243014_Visium_KI_4_barcodes.tsv.gz</td>
<td bgcolor="#DEEBDC" title="24777">24.2 Kb</td>
<td bgcolor="#DEEBDC"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8243nnn/GSM8243014/suppl/GSM8243014%5FVisium%5FKI%5F4%5Fbarcodes%2Etsv%2Egz">(ftp)</a><a href="/geo/download/?acc=GSM8243014&amp;format=file&amp;file=GSM8243014%5FVisium%5FKI%5F4%5Fbarcodes%2Etsv%2Egz">(http)</a></td>
<td bgcolor="#DEEBDC">TSV</td>
</tr>
<tr valign="top"><td bgcolor="#EEEEEE">GSM8243014_Visium_KI_4_features.tsv.gz</td>
<td bgcolor="#EEEEEE" title="260696">254.6 Kb</td>
<td bgcolor="#EEEEEE"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8243nnn/GSM8243014/suppl/GSM8243014%5FVisium%5FKI%5F4%5Ffeatures%2Etsv%2Egz">(ftp)</a><a href="/geo/download/?acc=GSM8243014&amp;format=file&amp;file=GSM8243014%5FVisium%5FKI%5F4%5Ffeatures%2Etsv%2Egz">(http)</a></td>
<td bgcolor="#EEEEEE">TSV</td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSM8243014_Visium_KI_4_matrix.mtx.gz</td>
<td bgcolor="#DEEBDC" title="60772109">58.0 Mb</td>
<td bgcolor="#DEEBDC"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/samples/GSM8243nnn/GSM8243014/suppl/GSM8243014%5FVisium%5FKI%5F4%5Fmatrix%2Emtx%2Egz">(ftp)</a><a href="/geo/download/?acc=GSM8243014&amp;format=file&amp;file=GSM8243014%5FVisium%5FKI%5F4%5Fmatrix%2Emtx%2Egz">(http)</a></td>
<td bgcolor="#DEEBDC">MTX</td>
</tr>
<tr><td><a href="/Traces/study/?acc=SRX24413938">SRA Run Selector</a><a href="javascript:RPopUpWindow_Set(geoaxema_srarun,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td></tr>
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


