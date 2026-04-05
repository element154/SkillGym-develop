



<!DOCTYPE html>
<html class="gl-system ui-neutral with-top-bar with-header application-chrome page-with-panels with-gl-container-queries with-system-footer" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="width=device-width, initial-scale=1" name="viewport">
<title>source code/README.md · main · Hoang Giang Vu / stvd-kg · GitLab</title>
<script>
//<![CDATA[
window.gon={};gon.math_rendering_limits_enabled=true;gon.features={"inlineBlame":false,"directoryCodeDropdownUpdates":true,"repositoryFileTreeBrowser":false,"blobEditRefactor":false};
//]]>
</script>

<script>
//<![CDATA[
const root = document.documentElement;
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  root.classList.add('gl-dark');
}

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  if (e.matches) {
    root.classList.add('gl-dark');
  } else {
    root.classList.remove('gl-dark');
  }
});

//]]>
</script>
<script>
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = {"/22313906t/stvd-kg/-/blob/main/source%20code/README.md?format=json\u0026viewer=rich":{}};
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: [String!]!\n  $ref: String!\n  $refType: RefType\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: $filePath, ref: $ref, refType: $refType) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canModifyBlobWithWebIde\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"22313906t/stvd-kg","ref":"main","refType":null,"filePath":"source code/README.md","shouldFetchRawText":false}}];

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"65kWgOXfNlrA3M4kS82nwNb0jOpL5VNtmtU3r6jH1-XfQ7dCPdj_j1mQDD4ydS_KF4Lr5p5_6W0XGJeBMdMMSQ","x-gitlab-feature-category":"source_code_management"};
  const url = `https://scm.univ-tours.fr/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>

<link rel="prefetch" href="/assets/webpack/monaco.2f50fc5f.chunk.js">

<meta content="light dark" name="color-scheme">
<link rel="stylesheet" href="/assets/application-267421195ad431679553836c5b410ffe630f2a3119c436775ff47aa32bd041a8.css" media="(prefers-color-scheme: light)" />
<link rel="stylesheet" href="/assets/application_dark-eb6a2be3fa84f122bcfdb01700ceb93d31abe14bec53e18529b0230fdb8d07ce.css" media="(prefers-color-scheme: dark)" />
<link rel="stylesheet" href="/assets/page_bundles/tree-87852cf755928d514a7c18c7bc442022c92b8887a274746dadf9ab0f18417de8.css" /><link rel="stylesheet" href="/assets/page_bundles/projects-5ff1d9a4f328199704b89fcdbf5501b932b19e481ac1139171ece972e7cf4c7f.css" /><link rel="stylesheet" href="/assets/page_bundles/commit_description-9e7efe20f0cef17d0606edabfad0418e9eb224aaeaa2dae32c817060fa60abcc.css" /><link rel="stylesheet" href="/assets/page_bundles/work_items-9f34e9e1785e95144a97edb25299b8dd0d2e641f7efb2d8b7bea3717104ed8f2.css" /><link rel="stylesheet" href="/assets/page_bundles/notes_shared-8f7a9513332533cc4a53b3be3d16e69570e82bc87b3f8913578eaeb0dce57e21.css" />
<link rel="stylesheet" href="/assets/tailwind_cqs-0e9add9895902b334f85f3a8c9ded0e9bcbfef603bbd1efcb51df7dac57c209e.css" />


<link rel="stylesheet" href="/assets/fonts-deb7ad1d55ca77c0172d8538d53442af63604ff490c74acc2859db295c125bdb.css" />
<link rel="stylesheet" href="/assets/highlight/themes/white-c47e38e4a3eafd97b389c0f8eec06dce295f311cdc1c9e55073ea9406b8fe5b0.css" media="(prefers-color-scheme: light)" />
<link rel="stylesheet" href="/assets/highlight/themes/dark-8796b0549a7cd8fd6d2646619fa5840db4505d7031a76d5441a3cee1d12390d2.css" media="(prefers-color-scheme: dark)" />

<script src="/assets/webpack/runtime.880a9edb.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.ca0196b2.chunk.js" defer="defer"></script>
<script src="/assets/webpack/tracker.4ac2efa2.chunk.js" defer="defer"></script>
<script>
//<![CDATA[
window.snowplowOptions = {"namespace":"gl","hostname":"scm.univ-tours.fr:443","postPath":"/-/collect_events","forceSecureTracker":true,"appId":"gitlab_sm"};
gl = window.gl || {};
gl.snowplowStandardContext = {"schema":"iglu:com.gitlab/gitlab_standard/jsonschema/1-1-7","data":{"environment":"self-managed","source":"gitlab-rails","correlation_id":"01KNBK961X56881KP3GGCZ7T5B","extra":{},"user_id":null,"global_user_id":null,"user_type":null,"is_gitlab_team_member":null,"namespace_id":1290,"ultimate_parent_namespace_id":1290,"project_id":820,"feature_enabled_by_namespace_ids":null,"realm":"self-managed","deployment_type":"self-managed","context_generated_at":"2026-04-04T08:35:58.187+02:00"}};
gl.snowplowPseudonymizedPageUrl = "https://scm.univ-tours.fr/namespace1290/project820/-/blob/:repository_path";
gl.maskedDefaultReferrerUrl = null;
gl.ga4MeasurementId = 'G-ENFH3X7M5Y';
gl.duoEvents = [];
gl.onlySendDuoEvents = false;


//]]>
</script>
<link rel="preload" href="/assets/application-267421195ad431679553836c5b410ffe630f2a3119c436775ff47aa32bd041a8.css" as="style" type="text/css">
<link rel="preload" href="/assets/highlight/themes/white-c47e38e4a3eafd97b389c0f8eec06dce295f311cdc1c9e55073ea9406b8fe5b0.css" as="style" type="text/css">




<script src="/assets/webpack/commons-pages.groups.new-pages.import.gitlab_projects.new-pages.import.manifest.new-pages.projects.n-44c6c18e.1bfb6269.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.search.show-super_sidebar.6acb116e.chunk.js" defer="defer"></script>
<script src="/assets/webpack/super_sidebar.d81b6984.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-16912510.ec48a109.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.admin.application_settings-pages.admin.application_settings.appearances.preview_sign_i-f1565176.4e33d525.chunk.js" defer="defer"></script>
<script src="/assets/webpack/17193943.e2846711.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.packages-pages.groups.registry.repositories-pages.projects.blob.show-pages.proj-5c8a36cb.3416fb61.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.branches.new-pages.projects.commits.show-pages.proje-81161c0b.b40d5f1b.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.import.bitbucket_server.new-pages.import.gitea.new-pages.import.gitlab_projects.new-pa-7a549248.80e44fb5.chunk.js" defer="defer"></script>
<script src="/assets/webpack/dbe6a049.8c51c52f.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.edit-pages.projects.sni-42df7d4c.aa95e753.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-c684fcf6.8c6bf173.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.edit-pages.projects.blob.new-pages.projects.blob.show-pages.projects.sho-ec79e51c.64cb1109.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.commits.show-pages.projects.show-pages.projects.tree.show.5d32875d.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show-pages.search.show.8df4e3fd.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blame.show-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.1fe49f7f.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.6f97c221.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.tree.show-treeList.1db58909.chunk.js" defer="defer"></script>
<script src="/assets/webpack/pages.projects.blob.show.ba0821e0.chunk.js" defer="defer"></script>

<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="source code/README.md · main · Hoang Giang Vu / stvd-kg · GitLab" property="og:title">
<meta content="SCM-Université de Tours" property="og:description">
<meta content="https://scm.univ-tours.fr/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://scm.univ-tours.fr/22313906t/stvd-kg/-/blob/main/source%20code/README.md" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="source code/README.md · main · Hoang Giang Vu / stvd-kg · GitLab" property="twitter:title">
<meta content="SCM-Université de Tours" property="twitter:description">
<meta content="https://scm.univ-tours.fr/assets/twitter_card-570ddb06edf56a2312253c5872489847a0f385112ddbcd71ccfa1570febab5d2.jpg" property="twitter:image">

<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="EUQaIh9470BJIa80fnXKYpuxrvI-L5vk1o7jBcgEW_slnrvgx38mldBtbS4HzUJoWsfJ_uu1IeRbQ0MrURCAVw" />
<meta name="csp-nonce" />
<meta name="action-cable-url" content="/-/cable" />
<link href="/-/manifest.json" rel="manifest">
<link rel="icon" type="image/png" href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png" />
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">




<meta content="SCM-Université de Tours" name="description">
<meta content="#F1F0F6" media="(prefers-color-scheme: light)" name="theme-color">
<meta content="#232128" media="(prefers-color-scheme: dark)" name="theme-color">
</head>

<body class="tab-width-8 gl-browser-generic gl-platform-other " data-namespace-id="1290" data-page="projects:blob:show" data-page-type-id="main/source code/README.md" data-project="stvd-kg" data-project-full-path="22313906t/stvd-kg" data-project-id="820" data-project-studio-enabled="true">
<div id="js-tooltips-container"></div>

<script>
//<![CDATA[
gl = window.gl || {};
gl.client = {"isGeneric":true,"isOther":true};


//]]>
</script>


<header class="super-topbar js-super-topbar"></header>
<div class="layout-page js-page-layout page-with-super-sidebar">
<script>
//<![CDATA[
const outer = document.createElement('div');
outer.style.visibility = 'hidden';
outer.style.overflow = 'scroll';
document.body.appendChild(outer);
const inner = document.createElement('div');
outer.appendChild(inner);
const scrollbarWidth = outer.offsetWidth - inner.offsetWidth;
outer.parentNode.removeChild(outer);
document.documentElement.style.setProperty('--scrollbar-width', `${scrollbarWidth}px`);

//]]>
</script><aside class="js-super-sidebar super-sidebar super-sidebar-loading" data-command-palette="{&quot;project_files_url&quot;:&quot;/22313906t/stvd-kg/-/files/main?format=json&quot;,&quot;project_blob_url&quot;:&quot;/22313906t/stvd-kg/-/blob/main&quot;}" data-force-desktop-expanded-sidebar="" data-is-saas="false" data-root-path="/" data-sidebar="{&quot;is_logged_in&quot;:false,&quot;compare_plans_url&quot;:&quot;https://about.gitlab.com/pricing&quot;,&quot;context_switcher_links&quot;:[{&quot;title&quot;:&quot;Explore&quot;,&quot;link&quot;:&quot;/explore&quot;,&quot;icon&quot;:&quot;compass&quot;}],&quot;current_menu_items&quot;:[{&quot;id&quot;:&quot;project_overview&quot;,&quot;title&quot;:&quot;stvd-kg&quot;,&quot;entity_id&quot;:820,&quot;link&quot;:&quot;/22313906t/stvd-kg&quot;,&quot;link_classes&quot;:&quot;shortcuts-project&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;manage_menu&quot;,&quot;title&quot;:&quot;Manage&quot;,&quot;icon&quot;:&quot;users&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/activity&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;activity&quot;,&quot;title&quot;:&quot;Activity&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/activity&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-activity&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;members&quot;,&quot;title&quot;:&quot;Members&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/project_members&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;labels&quot;,&quot;title&quot;:&quot;Labels&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/labels&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;plan_menu&quot;,&quot;title&quot;:&quot;Plan&quot;,&quot;icon&quot;:&quot;planning&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/issues&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;project_issue_list&quot;,&quot;title&quot;:&quot;Issues&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/issues&quot;,&quot;link_classes&quot;:&quot;shortcuts-issues has-sub-items&quot;,&quot;pill_count_field&quot;:&quot;openIssuesCount&quot;,&quot;pill_count_dynamic&quot;:false,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;boards&quot;,&quot;title&quot;:&quot;Issue boards&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/boards&quot;,&quot;link_classes&quot;:&quot;shortcuts-issue-boards&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;milestones&quot;,&quot;title&quot;:&quot;Milestones&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/milestones&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_wiki&quot;,&quot;title&quot;:&quot;Wiki&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/wikis/home&quot;,&quot;link_classes&quot;:&quot;shortcuts-wiki&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;code_menu&quot;,&quot;title&quot;:&quot;Code&quot;,&quot;icon&quot;:&quot;code&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/merge_requests&quot;,&quot;is_active&quot;:true,&quot;items&quot;:[{&quot;id&quot;:&quot;project_merge_request_list&quot;,&quot;title&quot;:&quot;Merge requests&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/merge_requests&quot;,&quot;link_classes&quot;:&quot;shortcuts-merge_requests&quot;,&quot;pill_count_field&quot;:&quot;openMergeRequestsCount&quot;,&quot;pill_count_dynamic&quot;:false,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;files&quot;,&quot;title&quot;:&quot;Repository&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/tree/main&quot;,&quot;link_classes&quot;:&quot;shortcuts-tree&quot;,&quot;is_active&quot;:true},{&quot;id&quot;:&quot;branches&quot;,&quot;title&quot;:&quot;Branches&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/branches&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;commits&quot;,&quot;title&quot;:&quot;Commits&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/commits/main?ref_type=heads&quot;,&quot;link_classes&quot;:&quot;shortcuts-commits&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;tags&quot;,&quot;title&quot;:&quot;Tags&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/tags&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;graphs&quot;,&quot;title&quot;:&quot;Repository graph&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/network/main?ref_type=heads&quot;,&quot;link_classes&quot;:&quot;shortcuts-network&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;compare&quot;,&quot;title&quot;:&quot;Compare revisions&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/compare?from=main\u0026to=main&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;project_snippets&quot;,&quot;title&quot;:&quot;Snippets&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/snippets&quot;,&quot;link_classes&quot;:&quot;shortcuts-snippets&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;build_menu&quot;,&quot;title&quot;:&quot;Build&quot;,&quot;icon&quot;:&quot;rocket&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/pipelines&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;pipelines&quot;,&quot;title&quot;:&quot;Pipelines&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/pipelines&quot;,&quot;link_classes&quot;:&quot;shortcuts-pipelines&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;jobs&quot;,&quot;title&quot;:&quot;Jobs&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/jobs&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;pipeline_schedules&quot;,&quot;title&quot;:&quot;Pipeline schedules&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/pipeline_schedules&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;artifacts&quot;,&quot;title&quot;:&quot;Artifacts&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/artifacts&quot;,&quot;link_classes&quot;:&quot;shortcuts-builds&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;deploy_menu&quot;,&quot;title&quot;:&quot;Deploy&quot;,&quot;icon&quot;:&quot;deployments&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/releases&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;releases&quot;,&quot;title&quot;:&quot;Releases&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/releases&quot;,&quot;link_classes&quot;:&quot;shortcuts-deployments-releases&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;packages_registry&quot;,&quot;title&quot;:&quot;Package registry&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/packages&quot;,&quot;link_classes&quot;:&quot;shortcuts-container-registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;container_registry&quot;,&quot;title&quot;:&quot;Container registry&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/container_registry&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_registry&quot;,&quot;title&quot;:&quot;Model registry&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/ml/models&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;operations_menu&quot;,&quot;title&quot;:&quot;Operate&quot;,&quot;icon&quot;:&quot;cloud-pod&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/environments&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;environments&quot;,&quot;title&quot;:&quot;Environments&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/environments&quot;,&quot;link_classes&quot;:&quot;shortcuts-environments&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;infrastructure_registry&quot;,&quot;title&quot;:&quot;Terraform modules&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/terraform_module_registry&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;monitor_menu&quot;,&quot;title&quot;:&quot;Monitor&quot;,&quot;icon&quot;:&quot;monitor&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/incidents&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;incidents&quot;,&quot;title&quot;:&quot;Incidents&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/incidents&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false},{&quot;id&quot;:&quot;analyze_menu&quot;,&quot;title&quot;:&quot;Analyze&quot;,&quot;icon&quot;:&quot;chart&quot;,&quot;avatar_shape&quot;:&quot;rect&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/value_stream_analytics&quot;,&quot;is_active&quot;:false,&quot;items&quot;:[{&quot;id&quot;:&quot;cycle_analytics&quot;,&quot;title&quot;:&quot;Value stream analytics&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/value_stream_analytics&quot;,&quot;link_classes&quot;:&quot;shortcuts-project-cycle-analytics&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;contributors&quot;,&quot;title&quot;:&quot;Contributor analytics&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/graphs/main?ref_type=heads&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;ci_cd_analytics&quot;,&quot;title&quot;:&quot;CI/CD analytics&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/pipelines/charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;repository_analytics&quot;,&quot;title&quot;:&quot;Repository analytics&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/graphs/main/charts&quot;,&quot;link_classes&quot;:&quot;shortcuts-repository-charts&quot;,&quot;is_active&quot;:false},{&quot;id&quot;:&quot;model_experiments&quot;,&quot;title&quot;:&quot;Model experiments&quot;,&quot;link&quot;:&quot;/22313906t/stvd-kg/-/ml/experiments&quot;,&quot;is_active&quot;:false}],&quot;separated&quot;:false}],&quot;current_context_header&quot;:&quot;Project&quot;,&quot;support_path&quot;:&quot;https://about.gitlab.com/get-help/&quot;,&quot;docs_path&quot;:&quot;/help/docs&quot;,&quot;display_whats_new&quot;:false,&quot;show_version_check&quot;:null,&quot;search&quot;:{&quot;search_path&quot;:&quot;/search&quot;,&quot;issues_path&quot;:&quot;/dashboard/issues&quot;,&quot;mr_path&quot;:&quot;/dashboard/merge_requests&quot;,&quot;autocomplete_path&quot;:&quot;/search/autocomplete&quot;,&quot;settings_path&quot;:&quot;/search/settings&quot;,&quot;search_context&quot;:{&quot;project&quot;:{&quot;id&quot;:820,&quot;name&quot;:&quot;stvd-kg&quot;},&quot;project_metadata&quot;:{&quot;mr_path&quot;:&quot;/22313906t/stvd-kg/-/merge_requests&quot;,&quot;issues_path&quot;:&quot;/22313906t/stvd-kg/-/issues&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;main&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}},&quot;panel_type&quot;:&quot;project&quot;,&quot;shortcut_links&quot;:[{&quot;title&quot;:&quot;Snippets&quot;,&quot;href&quot;:&quot;/explore/snippets&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-snippets&quot;},{&quot;title&quot;:&quot;Groups&quot;,&quot;href&quot;:&quot;/explore/groups&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-groups&quot;},{&quot;title&quot;:&quot;Projects&quot;,&quot;href&quot;:&quot;/explore/projects/starred&quot;,&quot;css_class&quot;:&quot;dashboard-shortcuts-projects&quot;}],&quot;terms&quot;:null,&quot;sign_in_visible&quot;:&quot;true&quot;,&quot;allow_signup&quot;:&quot;false&quot;,&quot;new_user_registration_path&quot;:&quot;/users/sign_up&quot;,&quot;sign_in_path&quot;:&quot;/users/sign_in?redirect_to_referer=yes&quot;}"></aside>


<div class="panels-container gl-flex gl-gap-3">
<div class="content-panels gl-flex-1 gl-w-full gl-flex gl-gap-3 gl-relative js-content-panels gl-@container/content-panels">
<div class="js-static-panel static-panel content-wrapper gl-relative paneled-view gl-flex-1 gl-overflow-y-auto gl-bg-default" id="static-panel-portal">
<div class="panel-header">
<div class="broadcast-wrapper">



</div>
<div class="top-bar-fixed container-fluid gl-rounded-t-lg gl-sticky gl-top-0 gl-left-0 gl-mx-0 gl-w-full" data-testid="top-bar">
<div class="top-bar-container gl-flex gl-items-center gl-gap-2">
<div class="gl-grow gl-basis-0 gl-flex gl-items-center gl-justify-start gl-gap-3">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Hoang Giang Vu","item":"https://scm.univ-tours.fr/22313906t"},{"@type":"ListItem","position":2,"name":"stvd-kg","item":"https://scm.univ-tours.fr/22313906t/stvd-kg"},{"@type":"ListItem","position":3,"name":"Repository","item":"https://scm.univ-tours.fr/22313906t/stvd-kg/-/blob/main/source%20code/README.md"}]}


</script>
<div data-testid="breadcrumb-links" id="js-vue-page-breadcrumbs-wrapper">
<div data-breadcrumbs-json="[{&quot;text&quot;:&quot;Hoang Giang Vu&quot;,&quot;href&quot;:&quot;/22313906t&quot;,&quot;avatarPath&quot;:null},{&quot;text&quot;:&quot;stvd-kg&quot;,&quot;href&quot;:&quot;/22313906t/stvd-kg&quot;,&quot;avatarPath&quot;:null},{&quot;text&quot;:&quot;Repository&quot;,&quot;href&quot;:&quot;/22313906t/stvd-kg/-/blob/main/source%20code/README.md&quot;,&quot;avatarPath&quot;:null}]" id="js-vue-page-breadcrumbs"></div>
<div id="js-injected-page-breadcrumbs"></div>
<div id="js-page-breadcrumbs-extra"></div>
</div>


<div id="js-work-item-feedback"></div>

</div>

</div>
</div>

</div>
<div class="panel-content">
<div class="panel-content-inner js-static-panel-inner">
<div class="alert-wrapper alert-wrapper-top-space gl-flex gl-flex-col gl-gap-3 container-fluid container-limited">


























</div>

<div class="container-fluid container-limited project-highlight-puc">
<main class="content gl-@container/panel gl-pb-3" id="content-body" itemscope itemtype="http://schema.org/SoftwareSourceCode">
<div id="js-drawer-container"></div>
<div class="flash-container flash-container-page sticky" data-testid="flash-container">
<div id="js-global-alerts"></div>
</div>






<div class="js-signature-container" data-signatures-path="/22313906t/stvd-kg/-/commits/f2231da80b7cbdcaee06ec2b4a4c3e37540321b9/signatures?limit=1"></div>

<div class="tree-holder gl-pt-5" id="tree-holder">
<div data-blob-path="source code/README.md" data-breadcrumbs-can-collaborate="false" data-breadcrumbs-can-edit-tree="false" data-breadcrumbs-can-push-code="false" data-breadcrumbs-can-push-to-branch="false" data-breadcrumbs-new-blob-path="/22313906t/stvd-kg/-/new/main" data-breadcrumbs-new-branch-path="/22313906t/stvd-kg/-/branches/new" data-breadcrumbs-new-dir-path="/22313906t/stvd-kg/-/create_dir/main" data-breadcrumbs-new-tag-path="/22313906t/stvd-kg/-/tags/new" data-breadcrumbs-upload-path="/22313906t/stvd-kg/-/create/main" data-download-links="[{&quot;text&quot;:&quot;zip&quot;,&quot;path&quot;:&quot;/22313906t/stvd-kg/-/archive/main/stvd-kg-main.zip&quot;},{&quot;text&quot;:&quot;tar.gz&quot;,&quot;path&quot;:&quot;/22313906t/stvd-kg/-/archive/main/stvd-kg-main.tar.gz&quot;},{&quot;text&quot;:&quot;tar.bz2&quot;,&quot;path&quot;:&quot;/22313906t/stvd-kg/-/archive/main/stvd-kg-main.tar.bz2&quot;},{&quot;text&quot;:&quot;tar&quot;,&quot;path&quot;:&quot;/22313906t/stvd-kg/-/archive/main/stvd-kg-main.tar&quot;}]" data-escaped-ref="main" data-history-link="/22313906t/stvd-kg/-/commits/main" data-http-url="https://scm.univ-tours.fr/22313906t/stvd-kg.git" data-project-id="820" data-project-path="22313906t/stvd-kg" data-project-root-path="/22313906t/stvd-kg" data-project-short-path="stvd-kg" data-ref="main" data-ref-type="" data-root-ref="main" data-ssh-url="git@scm.univ-tours.fr:22313906t/stvd-kg.git" data-xcode-url="" id="js-repository-blob-header-app"></div>
<div class="info-well">
<div data-history-link="/22313906t/stvd-kg/-/commits/main" id="js-last-commit"></div>
<div class="gl-hidden @sm/panel:gl-block">

</div>
</div>
<div class="blob-content-holder js-per-page" data-blame-per-page="1000" id="blob-content-holder">
<div data-blob-path="source code/README.md" data-can-download-code="true" data-escaped-ref="main" data-full-name="Hoang Giang Vu / stvd-kg" data-has-revs-file="false" data-original-branch="main" data-project-path="22313906t/stvd-kg" data-ref-type="" data-resource-id="gid://gitlab/Project/820" data-user-id="" id="js-view-blob-app">
<div class="gl-spinner-container" role="status"><span aria-hidden class="gl-spinner gl-spinner-md gl-spinner-dark !gl-align-text-bottom"></span><span class="gl-sr-only !gl-absolute">Loading</span>
</div>
</div>
</div>

</div>
<script>
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/22313906t/stvd-kg/edit/main/-/source%20code/README.md'


//]]>
</script>
<div data-ambiguous="false" data-ref="main" id="js-ambiguous-ref-modal"></div>

</main>
</div>

</div>

</div>
</div>
<div class="js-dynamic-panel paneled-view contextual-panel gl-@container/panel !gl-absolute gl-shadow-lg @xl/content-panels:gl-w-1/2 @xl/content-panels:gl-shadow-none @xl/content-panels:!gl-relative" id="contextual-panel-portal"></div>
</div>
</div>

</div>

<div class="footer-message" style="background-color: #292861;color: #ffffff"><p>SCM-Plateforme collaborative de développement  de l'Université de Tours</p></div>
<script>
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.testid = 'js-lazy-loaded-content';
  });
}

//]]>
</script>
<script>
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>

</body>
</html>

