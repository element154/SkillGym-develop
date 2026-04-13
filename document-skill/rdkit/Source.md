## Source: https://www.rdkit.org/docs/source/rdkit.html

# rdkit package¶

## Subpackages¶

- rdkit.Avalon package
- Submodules
- rdkit.Avalon.pyAvalonTools module
`CheckMolecule()`

`CheckMoleculeString()`

`CloseCheckMolFiles()`

`Generate2DCoords()`

`GetAvalonCountFP()`

`GetAvalonFP()`

`GetAvalonFPAsWords()`

`GetCanonSmiles()`

`GetCheckMolLog()`

`InitializeCheckMol()`

`StruChkFlag`

`StruChkFlag.alias_conversion_failed`

`StruChkFlag.atom_check_failed`

`StruChkFlag.atom_clash`

`StruChkFlag.bad_molecule`

`StruChkFlag.dubious_stereo_removed`

`StruChkFlag.either_warning`

`StruChkFlag.fragments_found`

`StruChkFlag.names`

`StruChkFlag.recharged`

`StruChkFlag.size_check_failed`

`StruChkFlag.stereo_error`

`StruChkFlag.stereo_forced_bad`

`StruChkFlag.stereo_transformed`

`StruChkFlag.template_transformed`

`StruChkFlag.transformed`

`StruChkFlag.values`

`StruChkResult`

- rdkit.Avalon.pyAvalonTools module
- Module contents

- Submodules
- rdkit.Chem package
- Subpackages
- rdkit.Chem.AtomPairs package
- rdkit.Chem.ChemUtils package
- rdkit.Chem.Draw package
- Submodules
- rdkit.Chem.Draw.IPythonConsole module
- rdkit.Chem.Draw.MolDrawing module
`DrawingOptions`

`DrawingOptions.atomLabelDeuteriumTritium`

`DrawingOptions.atomLabelFontFace`

`DrawingOptions.atomLabelFontSize`

`DrawingOptions.atomLabelMinFontSize`

`DrawingOptions.atomNumberOffset`

`DrawingOptions.bgColor`

`DrawingOptions.bondLineWidth`

`DrawingOptions.colorBonds`

`DrawingOptions.coordScale`

`DrawingOptions.dash`

`DrawingOptions.dblBondLengthFrac`

`DrawingOptions.dblBondOffset`

`DrawingOptions.defaultColor`

`DrawingOptions.dotsPerAngstrom`

`DrawingOptions.elemDict`

`DrawingOptions.includeAtomNumbers`

`DrawingOptions.noCarbonSymbols`

`DrawingOptions.radicalSymbol`

`DrawingOptions.selectColor`

`DrawingOptions.showUnknownDoubleBonds`

`DrawingOptions.useFraction`

`DrawingOptions.wedgeDashedBonds`

`Font`

`MolDrawing`

`cmp()`

- rdkit.Chem.Draw.SimilarityMaps module
`GetAPFingerprint()`

`GetAtomicWeightsForFingerprint()`

`GetAtomicWeightsForFingerprintGenerator()`

`GetAtomicWeightsForModel()`

`GetMorganFingerprint()`

`GetRDKFingerprint()`

`GetSimilarityMapForFingerprint()`

`GetSimilarityMapForFingerprintGenerator()`

`GetSimilarityMapForModel()`

`GetSimilarityMapFromWeights()`

`GetStandardizedWeights()`

`GetTTFingerprint()`

- rdkit.Chem.Draw.rdMolDraw2D module
`ContourAndDrawGaussians()`

`ContourAndDrawGrid()`

`ContourParams`

`ContourParams.colourMap`

`ContourParams.contourColour`

`ContourParams.contourWidth`

`ContourParams.coordScaleForQuantization`

`ContourParams.dashNegative`

`ContourParams.drawAsLines`

`ContourParams.extraGridPadding`

`ContourParams.fillGrid`

`ContourParams.fillThreshold`

`ContourParams.fillThresholdIsFraction`

`ContourParams.gridResolution`

`ContourParams.isovalScaleForQuantization`

`ContourParams.setColourMap()`

`ContourParams.setContourColour()`

`ContourParams.setScale`

`ContourParams.useFillThreshold`

`DrawElement`

`DrawMoleculeACS1996()`

`IntStringMap`

`MeanBondLength()`

`MolDraw2D`

`MolDraw2D.ClearDrawing()`

`MolDraw2D.DrawArc()`

`MolDraw2D.DrawArrow()`

`MolDraw2D.DrawAttachmentLine()`

`MolDraw2D.DrawEllipse()`

`MolDraw2D.DrawLine()`

`MolDraw2D.DrawMolecule()`

`MolDraw2D.DrawMoleculeWithHighlights()`

`MolDraw2D.DrawMolecules()`

`MolDraw2D.DrawPolygon()`

`MolDraw2D.DrawReaction()`

`MolDraw2D.DrawRect()`

`MolDraw2D.DrawString()`

`MolDraw2D.DrawTriangle()`

`MolDraw2D.DrawWavyLine()`

`MolDraw2D.FillPolys()`

`MolDraw2D.FlexiMode()`

`MolDraw2D.FontSize()`

`MolDraw2D.GetDrawCoords()`

`MolDraw2D.GetMolSize()`

`MolDraw2D.Height()`

`MolDraw2D.LineWidth()`

`MolDraw2D.Offset()`

`MolDraw2D.SetColour()`

`MolDraw2D.SetDrawOptions()`

`MolDraw2D.SetFillPolys()`

`MolDraw2D.SetFlexiMode()`

`MolDraw2D.SetFontSize()`

`MolDraw2D.SetLineWidth()`

`MolDraw2D.SetOffset()`

`MolDraw2D.SetScale()`

`MolDraw2D.Width()`

`MolDraw2D.drawOptions()`

`MolDraw2DCairo`

`MolDraw2DSVG`

`MolDrawOptions`

`MolDrawOptions.addAtomIndices`

`MolDrawOptions.addBondIndices`

`MolDrawOptions.addStereoAnnotation`

`MolDrawOptions.additionalAtomLabelPadding`

`MolDrawOptions.annotationColour`

`MolDrawOptions.annotationFontScale`

`MolDrawOptions.atomHighlightsAreCircles`

`MolDrawOptions.atomLabelDeuteriumTritium`

`MolDrawOptions.atomLabels`

`MolDrawOptions.atomNoteColour`

`MolDrawOptions.atomRegions`

`MolDrawOptions.backgroundColour`

`MolDrawOptions.baseFontSize`

`MolDrawOptions.bondLineWidth`

`MolDrawOptions.bondNoteColour`

`MolDrawOptions.bracketsAroundAtomLists`

`MolDrawOptions.centreMoleculesBeforeDrawing`

`MolDrawOptions.circleAtoms`

`MolDrawOptions.clearBackground`

`MolDrawOptions.comicMode`

`MolDrawOptions.continuousHighlight`

`MolDrawOptions.drawMolsSameScale`

`MolDrawOptions.drawingExtentsInclude`

`MolDrawOptions.dummiesAreAttachments`

`MolDrawOptions.dummyIsotopeLabels`

`MolDrawOptions.explicitMethyl`

`MolDrawOptions.fillHighlights`

`MolDrawOptions.fixedBondLength`

`MolDrawOptions.fixedFontSize`

`MolDrawOptions.fixedScale`

`MolDrawOptions.flagCloseContactsDist`

`MolDrawOptions.fontFile`

`MolDrawOptions.getAnnotationColour()`

`MolDrawOptions.getAtomNoteColour()`

`MolDrawOptions.getAtomPalette()`

`MolDrawOptions.getBackgroundColour()`

`MolDrawOptions.getBondNoteColour()`

`MolDrawOptions.getHighlightColour()`

`MolDrawOptions.getLegendColour()`

`MolDrawOptions.getQueryColour()`

`MolDrawOptions.getSymbolColour()`

`MolDrawOptions.getVariableAttachmentColour()`

`MolDrawOptions.highlightBondWidthMultiplier`

`MolDrawOptions.highlightColour`

`MolDrawOptions.highlightRadius`

`MolDrawOptions.includeAtomTags`

`MolDrawOptions.includeChiralFlagLabel`

`MolDrawOptions.includeMetadata`

`MolDrawOptions.includeRadicals`

`MolDrawOptions.isotopeLabels`

`MolDrawOptions.legendColour`

`MolDrawOptions.legendFontSize`

`MolDrawOptions.legendFraction`

`MolDrawOptions.maxFontSize`

`MolDrawOptions.minFontSize`

`MolDrawOptions.multiColourHighlightStyle`

`MolDrawOptions.multipleBondOffset`

`MolDrawOptions.noAtomLabels`

`MolDrawOptions.padding`

`MolDrawOptions.prepareMolsBeforeDrawing`

`MolDrawOptions.queryColour`

`MolDrawOptions.reagentPadding`

`MolDrawOptions.rotate`

`MolDrawOptions.scaleBondWidth`

`MolDrawOptions.scaleHighlightBondWidth`

`MolDrawOptions.scalingFactor`

`MolDrawOptions.setAnnotationColour()`

`MolDrawOptions.setAtomNoteColour()`

`MolDrawOptions.setAtomPalette()`

`MolDrawOptions.setBackgroundColour()`

`MolDrawOptions.setBondNoteColour()`

`MolDrawOptions.setHighlightColour()`

`MolDrawOptions.setLegendColour()`

`MolDrawOptions.setQueryColour()`

`MolDrawOptions.setSymbolColour()`

`MolDrawOptions.setVariableAttachmentColour()`

`MolDrawOptions.showAllCIPCodes`

`MolDrawOptions.simplifiedStereoGroupLabel`

`MolDrawOptions.singleColourWedgeBonds`

`MolDrawOptions.splitBonds`

`MolDrawOptions.standardColoursForHighlightedAtoms`

`MolDrawOptions.symbolColour`

`MolDrawOptions.unspecifiedStereoIsUnknown`

`MolDrawOptions.updateAtomPalette()`

`MolDrawOptions.useAvalonAtomPalette()`

`MolDrawOptions.useBWAtomPalette()`

`MolDrawOptions.useCDKAtomPalette()`

`MolDrawOptions.useComplexQueryAtomSymbols`

`MolDrawOptions.useDefaultAtomPalette()`

`MolDrawOptions.useMolBlockWedging`

`MolDrawOptions.variableAtomRadius`

`MolDrawOptions.variableAttachmentColour`

`MolDrawOptions.variableBondWidthMultiplier`

`MolToACS1996SVG()`

`MolToSVG()`

`MultiColourHighlightStyle`

`PrepareAndDrawMolecule()`

`PrepareMolForDrawing()`

`SetACS1996Mode()`

`SetDarkMode()`

`SetMonochromeMode()`

`UpdateDrawerParamsFromJSON()`

`UpdateMolDrawOptionsFromJSON()`

`map_indexing_suite_IntStringMap_entry`

- rdkit.Chem.Draw.rdMolDraw2DQt module

- Module contents
`DebugDraw()`

`DrawMolWithMatches()`

`DrawMorganBit()`

`DrawMorganBits()`

`DrawMorganEnv()`

`DrawMorganEnvs()`

`DrawRDKitBit()`

`DrawRDKitBits()`

`DrawRDKitEnv()`

`DrawRDKitEnvs()`

`FingerprintEnv`

`MolToFile()`

`MolToImage()`

`MolsMatrixToGridImage()`

`MolsToGridImage()`

`MolsToImage()`

`ReactionToImage()`

`SetComicMode()`

`ShowMol()`

`calcAtomGaussians()`

`shouldKekulize()`

- Submodules
- rdkit.Chem.EState package
- Submodules
- rdkit.Chem.EState.AtomTypes module
- rdkit.Chem.EState.EState module
- rdkit.Chem.EState.EState_VSA module
`EState_VSA1()`

`EState_VSA10()`

`EState_VSA11()`

`EState_VSA2()`

`EState_VSA3()`

`EState_VSA4()`

`EState_VSA5()`

`EState_VSA6()`

`EState_VSA7()`

`EState_VSA8()`

`EState_VSA9()`

`EState_VSA_()`

`VSA_EState1()`

`VSA_EState10()`

`VSA_EState2()`

`VSA_EState3()`

`VSA_EState4()`

`VSA_EState5()`

`VSA_EState6()`

`VSA_EState7()`

`VSA_EState8()`

`VSA_EState9()`

`VSA_EState_()`

- rdkit.Chem.EState.Fingerprinter module

- Module contents

- Submodules
- rdkit.Chem.FeatMaps package
- Submodules
- rdkit.Chem.FeatMaps.FeatMapParser module
- rdkit.Chem.FeatMaps.FeatMapPoint module
- rdkit.Chem.FeatMaps.FeatMapUtils module
- rdkit.Chem.FeatMaps.FeatMaps module

- Module contents

- Submodules
- rdkit.Chem.Features package
- rdkit.Chem.Fingerprints package
- Submodules
- rdkit.Chem.Fingerprints.ClusterMols module
- rdkit.Chem.Fingerprints.DbFpSupplier module
- rdkit.Chem.Fingerprints.FingerprintMols module
- rdkit.Chem.Fingerprints.MolSimilarity module
- rdkit.Chem.Fingerprints.SimilarityScreener module

- Module contents

- Submodules
- rdkit.Chem.Fraggle package
- rdkit.Chem.MolDb package
- Submodules
- Module contents

- rdkit.Chem.MolKey package
- rdkit.Chem.Pharm2D package
- Submodules
- rdkit.Chem.Pharm2D.Generate module
- rdkit.Chem.Pharm2D.Gobbi_Pharm2D module
- rdkit.Chem.Pharm2D.Matcher module
- rdkit.Chem.Pharm2D.SigFactory module
`SigFactory`

`SigFactory.GetBins()`

`SigFactory.GetBitDescription()`

`SigFactory.GetBitDescriptionAsText()`

`SigFactory.GetBitIdx()`

`SigFactory.GetBitInfo()`

`SigFactory.GetFeatFamilies()`

`SigFactory.GetMolFeats()`

`SigFactory.GetNumBins()`

`SigFactory.GetSigSize()`

`SigFactory.GetSignature()`

`SigFactory.Init()`

`SigFactory.SetBins()`

- rdkit.Chem.Pharm2D.Utils module

- Module contents

- Submodules
- rdkit.Chem.Pharm3D package
- Submodules
- rdkit.Chem.Pharm3D.EmbedLib module
`AddExcludedVolumes()`

`Check2DBounds()`

`CoarseScreenPharmacophore()`

`CombiEnum()`

`ComputeChiralVolume()`

`ConstrainedEnum()`

`DownsampleBoundsMatrix()`

`EmbedMol()`

`EmbedOne()`

`EmbedPharmacophore()`

`GetAllPharmacophoreMatches()`

`GetAtomHeavyNeighbors()`

`MatchFeatsToMol()`

`MatchPharmacophore()`

`MatchPharmacophoreToMol()`

`OptimizeMol()`

`ReplaceGroup()`

`UpdatePharmacophoreBounds()`

`isNaN()`

- rdkit.Chem.Pharm3D.ExcludedVolume module
- rdkit.Chem.Pharm3D.Pharmacophore module
`ExplicitPharmacophore`

`Pharmacophore`

`Pharmacophore.getFeature()`

`Pharmacophore.getFeatures()`

`Pharmacophore.getLowerBound()`

`Pharmacophore.getLowerBound2D()`

`Pharmacophore.getUpperBound()`

`Pharmacophore.getUpperBound2D()`

`Pharmacophore.setLowerBound()`

`Pharmacophore.setLowerBound2D()`

`Pharmacophore.setUpperBound()`

`Pharmacophore.setUpperBound2D()`

- rdkit.Chem.Pharm3D.EmbedLib module
- Module contents

- Submodules
- rdkit.Chem.Scaffolds package
- Submodules
- rdkit.Chem.Scaffolds.MurckoScaffold module
- rdkit.Chem.Scaffolds.rdScaffoldNetwork module
`BRICSScaffoldParams()`

`CreateScaffoldNetwork()`

`EdgeType`

`NetworkEdge`

`NetworkEdge_VECT`

`ScaffoldNetwork`

`ScaffoldNetworkParams`

`ScaffoldNetworkParams.collectMolCounts`

`ScaffoldNetworkParams.flattenChirality`

`ScaffoldNetworkParams.flattenIsotopes`

`ScaffoldNetworkParams.flattenKeepLargest`

`ScaffoldNetworkParams.includeGenericBondScaffolds`

`ScaffoldNetworkParams.includeGenericScaffolds`

`ScaffoldNetworkParams.includeNames`

`ScaffoldNetworkParams.includeScaffoldsWithAttachments`

`ScaffoldNetworkParams.includeScaffoldsWithoutAttachments`

`ScaffoldNetworkParams.keepOnlyFirstFragment`

`ScaffoldNetworkParams.pruneBeforeFragmenting`

`UpdateScaffoldNetwork()`

- Module contents

- Submodules
- rdkit.Chem.SimpleEnum package
- rdkit.Chem.Subshape package
- Submodules
- rdkit.Chem.Subshape.BuilderUtils module
`AppendSkeletonPoints()`

`AssignMolFeatsToPoints()`

`CalculateDirectionsAtPoint()`

`ClusterTerminalPts()`

`ComputeGridIndices()`

`ComputeShapeGridCentroid()`

`ExpandTerminalPts()`

`FindFarthestGridPoint()`

`FindGridPointBetweenPoints()`

`FindTerminalPtsFromConformer()`

`FindTerminalPtsFromShape()`

`GetMoreTerminalPoints()`

- rdkit.Chem.Subshape.SubshapeAligner module
`ClusterAlignments()`

`GetShapeShapeDistance()`

`SubshapeAligner`

`SubshapeAligner.GetSubshapeAlignments()`

`SubshapeAligner.GetTriangleMatches()`

`SubshapeAligner.PruneMatchesUsingDirection()`

`SubshapeAligner.PruneMatchesUsingFeatures()`

`SubshapeAligner.PruneMatchesUsingShape()`

`SubshapeAligner.coarseGridToleranceMult`

`SubshapeAligner.dirThresh`

`SubshapeAligner.distMetric`

`SubshapeAligner.edgeTol`

`SubshapeAligner.medGridToleranceMult`

`SubshapeAligner.numFeatThresh`

`SubshapeAligner.shapeDistTol`

`SubshapeAligner.triangleRMSTol`

`SubshapeAlignment`

`SubshapeDistanceMetric`

`TransformMol()`

- rdkit.Chem.Subshape.SubshapeBuilder module
`SubshapeBuilder`

`SubshapeBuilder.CombineSubshapes()`

`SubshapeBuilder.GenerateSubshapeShape()`

`SubshapeBuilder.GenerateSubshapeSkeleton()`

`SubshapeBuilder.SampleSubshape()`

`SubshapeBuilder.featFactory`

`SubshapeBuilder.fraction`

`SubshapeBuilder.gridDims`

`SubshapeBuilder.gridSpacing`

`SubshapeBuilder.nbrCount`

`SubshapeBuilder.stepSize`

`SubshapeBuilder.terminalPtRadScale`

`SubshapeBuilder.winRad`

`SubshapeCombineOperations`

- rdkit.Chem.Subshape.SubshapeObjects module

- rdkit.Chem.Subshape.BuilderUtils module
- Module contents

- Submodules
- rdkit.Chem.Suppliers package
- rdkit.Chem.fmcs package
- Submodules
- rdkit.Chem.fmcs.fmcs module
`Atom`

`AtomSmartsNoAromaticity`

`Bond`

`CachingTargetsMatcher`

`CangenNode`

`Default`

`DirectedEdge`

`EnumerationMolecule`

`FragmentedTypedMolecule`

`MATCH()`

`MCSResult`

`OutgoingEdge`

`SingleBestAtoms`

`SingleBestAtomsCompleteRingsOnly`

`SingleBestBonds`

`SingleBestBondsCompleteRingsOnly`

`Subgraph`

`Timer`

`TypedFragment`

`TypedMolecule`

`Uniquer`

`VerboseCachingTargetsMatcher`

`VerboseHeapOps`

`all_subgraph_extensions()`

`assign_isotopes_from_class_tag()`

`atom_typer_any()`

`atom_typer_elements()`

`atom_typer_isotopes()`

`bond_typer_any()`

`bond_typer_bondtypes()`

`canon()`

`check_completeRingsOnly()`

`compute_mcs()`

`convert_input_to_typed_molecules()`

`default_atom_typer()`

`default_bond_typer()`

`enumerate_subgraphs()`

`find_duplicates()`

`find_extension_size()`

`find_extensions()`

`find_upper_fragment_size_limits()`

`fmcs()`

`fragmented_mol_to_enumeration_mols()`

`gen_primes()`

`generate_smarts()`

`get_canonical_bondtype_counts()`

`get_canonical_bondtypes()`

`get_closure_label()`

`get_counts()`

`get_initial_cangen_nodes()`

`get_isotopes()`

`get_selected_atom_classes()`

`get_specified_types()`

`get_typed_fragment()`

`get_typed_molecule()`

`intersect_counts()`

`main()`

`make_arbitrary_smarts()`

`make_canonical_smarts()`

`make_complete_sdf()`

`make_fragment_sdf()`

`make_fragment_smiles()`

`make_structure_format()`

`nonempty_powerset()`

`parse_num_atoms()`

`parse_select()`

`parse_threshold()`

`parse_timeout()`

`powerset()`

`prune_maximize_atoms()`

`prune_maximize_bonds()`

`remove_unknown_bondtypes()`

`rerank()`

`restore_isotopes()`

`save_atom_classes()`

`save_isotopes()`

`set_isotopes()`

`starting_from`

`subgraph_to_fragment()`

`tiebreaker()`

- rdkit.Chem.fmcs.fmcs module
- Module contents

- Submodules

- Submodules
- rdkit.Chem.AllChem module
- rdkit.Chem.BRICS module
- rdkit.Chem.BuildFragmentCatalog module
`BuildCatalog()`

`CalcGains()`

`CalcGainsFromFps()`

`OutputGainsData()`

`ParseArgs()`

`ProcessGainsData()`

`RunDetails`

`RunDetails.actCol`

`RunDetails.biasList`

`RunDetails.catalogName`

`RunDetails.dbName`

`RunDetails.delim`

`RunDetails.detailsName`

`RunDetails.doBuild`

`RunDetails.doDetails`

`RunDetails.doGains`

`RunDetails.doScore`

`RunDetails.doSigs`

`RunDetails.fpName`

`RunDetails.gainsName`

`RunDetails.hasTitle`

`RunDetails.inFileName`

`RunDetails.maxPath`

`RunDetails.minPath`

`RunDetails.nActs`

`RunDetails.nBits`

`RunDetails.nameCol`

`RunDetails.numMols`

`RunDetails.onBitsName`

`RunDetails.scoresName`

`RunDetails.smiCol`

`RunDetails.tableName`

`RunDetails.topN`

`ScoreFromLists()`

`ScoreMolecules()`

`ShowDetails()`

`SupplierFromDetails()`

`Usage()`

`message()`

- rdkit.Chem.ChemicalFeatures module
- rdkit.Chem.ChemicalForceFields module
- rdkit.Chem.Crippen module
- rdkit.Chem.Descriptors module
- rdkit.Chem.Descriptors3D module
- rdkit.Chem.EnumerateHeterocycles module
- rdkit.Chem.EnumerateStereoisomers module
- rdkit.Chem.FastSDMolSupplier module
- rdkit.Chem.FeatFinderCLI module
- rdkit.Chem.FilterCatalog module
- rdkit.Chem.FragmentCatalog module
- rdkit.Chem.FragmentMatcher module
- rdkit.Chem.Fragments module
`fr_Al_COO()`

`fr_Al_OH()`

`fr_Al_OH_noTert()`

`fr_ArN()`

`fr_Ar_COO()`

`fr_Ar_N()`

`fr_Ar_NH()`

`fr_Ar_OH()`

`fr_COO()`

`fr_COO2()`

`fr_C_O()`

`fr_C_O_noCOO()`

`fr_C_S()`

`fr_HOCCN()`

`fr_Imine()`

`fr_NH0()`

`fr_NH1()`

`fr_NH2()`

`fr_N_O()`

`fr_Ndealkylation1()`

`fr_Ndealkylation2()`

`fr_Nhpyrrole()`

`fr_SH()`

`fr_aldehyde()`

`fr_alkyl_carbamate()`

`fr_alkyl_halide()`

`fr_allylic_oxid()`

`fr_amide()`

`fr_amidine()`

`fr_aniline()`

`fr_aryl_methyl()`

`fr_azide()`

`fr_azo()`

`fr_barbitur()`

`fr_benzene()`

`fr_benzodiazepine()`

`fr_bicyclic()`

`fr_diazo()`

`fr_dihydropyridine()`

`fr_epoxide()`

`fr_ester()`

`fr_ether()`

`fr_furan()`

`fr_guanido()`

`fr_halogen()`

`fr_hdrzine()`

`fr_hdrzone()`

`fr_imidazole()`

`fr_imide()`

`fr_isocyan()`

`fr_isothiocyan()`

`fr_ketone()`

`fr_ketone_Topliss()`

`fr_lactam()`

`fr_lactone()`

`fr_methoxy()`

`fr_morpholine()`

`fr_nitrile()`

`fr_nitro()`

`fr_nitro_arom()`

`fr_nitro_arom_nonortho()`

`fr_nitroso()`

`fr_oxazole()`

`fr_oxime()`

`fr_para_hydroxylation()`

`fr_phenol()`

`fr_phenol_noOrthoHbond()`

`fr_phos_acid()`

`fr_phos_ester()`

`fr_piperdine()`

`fr_piperzine()`

`fr_priamide()`

`fr_prisulfonamd()`

`fr_pyridine()`

`fr_quatN()`

`fr_sulfide()`

`fr_sulfonamd()`

`fr_sulfone()`

`fr_term_acetylene()`

`fr_tetrazole()`

`fr_thiazole()`

`fr_thiocyan()`

`fr_thiophene()`

`fr_unbrch_alkane()`

`fr_urea()`

- rdkit.Chem.FunctionalGroups module
- rdkit.Chem.GraphDescriptors module
- rdkit.Chem.Graphs module
- rdkit.Chem.Lipinski module
`FractionCSP3()`

`HeavyAtomCount()`

`NHOHCount()`

`NOCount()`

`NumAliphaticCarbocycles()`

`NumAliphaticHeterocycles()`

`NumAliphaticRings()`

`NumAmideBonds()`

`NumAromaticCarbocycles()`

`NumAromaticHeterocycles()`

`NumAromaticRings()`

`NumAtomStereoCenters()`

`NumBridgeheadAtoms()`

`NumHAcceptors()`

`NumHDonors()`

`NumHeteroatoms()`

`NumHeterocycles()`

`NumRotatableBonds()`

`NumSaturatedCarbocycles()`

`NumSaturatedHeterocycles()`

`NumSaturatedRings()`

`NumSpiroAtoms()`

`NumUnspecifiedAtomStereoCenters()`

`Phi()`

`RingCount()`

- rdkit.Chem.MACCSkeys module
- rdkit.Chem.MolCatalog module
- rdkit.Chem.MolStandardize module
- Submodules
- rdkit.Chem.MolStandardize.rdMolStandardize module
`AllowedAtomsValidation`

`CHARGE_CORRECTIONS()`

`CanonicalTautomer()`

`ChargeCorrection`

`ChargeParent()`

`ChargeParentInPlace()`

`Cleanup()`

`CleanupInPlace()`

`CleanupParameters`

`CleanupParameters.acidbaseFile`

`CleanupParameters.doCanonical`

`CleanupParameters.fragmentFile`

`CleanupParameters.largestFragmentChooserCountHeavyAtomsOnly`

`CleanupParameters.largestFragmentChooserUseAtomCount`

`CleanupParameters.maxRestarts`

`CleanupParameters.maxTautomers`

`CleanupParameters.maxTransforms`

`CleanupParameters.normalizationsFile`

`CleanupParameters.preferOrganic`

`CleanupParameters.tautomerReassignStereo`

`CleanupParameters.tautomerRemoveBondStereo`

`CleanupParameters.tautomerRemoveIsotopicHs`

`CleanupParameters.tautomerRemoveSp3Stereo`

`CleanupParameters.tautomerTransformsFile`

`DisallowedAtomsValidation`

`DisallowedRadicalValidation`

`DisconnectOrganometallics()`

`DisconnectOrganometallicsInPlace()`

`FeaturesValidation`

`FragmentParent()`

`FragmentParentInPlace()`

`FragmentRemover`

`FragmentRemoverFromData()`

`FragmentValidation`

`GetDefaultTautomerScoreSubstructs()`

`GetV1TautomerEnumerator()`

`Is2DValidation`

`IsotopeParent()`

`IsotopeParentInPlace()`

`IsotopeValidation`

`LargestFragmentChooser`

`Layout2DValidation`

`MOL_SPTR_VECT`

`MetalDisconnector`

`MetalDisconnectorOptions`

`MolVSValidation`

`NeutralValidation`

`NoAtomValidation`

`Normalize()`

`NormalizeInPlace()`

`Normalizer`

`NormalizerFromData()`

`NormalizerFromParams()`

`Pipeline`

`PipelineLog`

`PipelineLogEntry`

`PipelineOptions`

`PipelineOptions.allowAromaticBondType`

`PipelineOptions.allowAtomBondClashExemption`

`PipelineOptions.allowDativeBondType`

`PipelineOptions.allowEmptyMolecules`

`PipelineOptions.allowEnhancedStereo`

`PipelineOptions.allowLongBondsInRings`

`PipelineOptions.atomClashLimit`

`PipelineOptions.bondLengthLimit`

`PipelineOptions.is2DZeroThreshold`

`PipelineOptions.metalNof`

`PipelineOptions.metalNon`

`PipelineOptions.minMedianBondLength`

`PipelineOptions.normalizerData`

`PipelineOptions.normalizerMaxRestarts`

`PipelineOptions.outputV2000`

`PipelineOptions.reportAllFailures`

`PipelineOptions.scaledMedianBondLength`

`PipelineOptions.strictParsing`

`PipelineResult`

`PipelineStage`

`PipelineStatus`

`PipelineStatus.BASIC_VALIDATION_ERROR`

`PipelineStatus.CHARGE_STANDARDIZATION_ERROR`

`PipelineStatus.FEATURES_VALIDATION_ERROR`

`PipelineStatus.FRAGMENTS_REMOVED`

`PipelineStatus.FRAGMENT_STANDARDIZATION_ERROR`

`PipelineStatus.INPUT_ERROR`

`PipelineStatus.IS2D_VALIDATION_ERROR`

`PipelineStatus.LAYOUT2D_VALIDATION_ERROR`

`PipelineStatus.METALS_DISCONNECTED`

`PipelineStatus.METAL_STANDARDIZATION_ERROR`

`PipelineStatus.NORMALIZATION_APPLIED`

`PipelineStatus.NORMALIZER_STANDARDIZATION_ERROR`

`PipelineStatus.NO_EVENT`

`PipelineStatus.OUTPUT_ERROR`

`PipelineStatus.PIPELINE_ERROR`

`PipelineStatus.PREPARE_FOR_STANDARDIZATION_ERROR`

`PipelineStatus.PREPARE_FOR_VALIDATION_ERROR`

`PipelineStatus.PROTONATION_CHANGED`

`PipelineStatus.STANDARDIZATION_ERROR`

`PipelineStatus.STEREO_VALIDATION_ERROR`

`PipelineStatus.STRUCTURE_MODIFICATION`

`PipelineStatus.VALIDATION_ERROR`

`PipelineStatus.names`

`PipelineStatus.values`

`RDKitValidation`

`Reionize()`

`ReionizeInPlace()`

`Reionizer`

`ReionizerFromData()`

`RemoveFragments()`

`RemoveFragmentsInPlace()`

`ScoreHeteroHs()`

`ScoreRings()`

`ScoreSubstructs()`

`SmilesTautomerMap`

`StandardizeSmiles()`

`StereoParent()`

`StereoParentInPlace()`

`StereoValidation`

`SubstructTerm`

`SubstructTermVector`

`SuperParent()`

`SuperParentInPlace()`

`Tautomer`

`TautomerEnumerator`

`TautomerEnumerator.Canonicalize()`

`TautomerEnumerator.Enumerate()`

`TautomerEnumerator.GetCallback()`

`TautomerEnumerator.GetMaxTautomers()`

`TautomerEnumerator.GetMaxTransforms()`

`TautomerEnumerator.GetReassignStereo()`

`TautomerEnumerator.GetRemoveBondStereo()`

`TautomerEnumerator.GetRemoveSp3Stereo()`

`TautomerEnumerator.PickCanonical()`

`TautomerEnumerator.ScoreTautomer()`

`TautomerEnumerator.SetCallback()`

`TautomerEnumerator.SetMaxTautomers()`

`TautomerEnumerator.SetMaxTransforms()`

`TautomerEnumerator.SetReassignStereo()`

`TautomerEnumerator.SetRemoveBondStereo()`

`TautomerEnumerator.SetRemoveSp3Stereo()`

`TautomerEnumerator.tautomerScoreVersion`

`TautomerEnumeratorCallback`

`TautomerEnumeratorResult`

`TautomerEnumeratorStatus`

`TautomerParent()`

`TautomerParentInPlace()`

`Uncharger`

`UpdateParamsFromJSON()`

`ValidateSmiles()`

`ValidationMethod`

`map_indexing_suite_SmilesTautomerMap_entry`

- rdkit.Chem.MolStandardize.rdMolStandardize module

- Submodules
- rdkit.Chem.MolSurf module
`LabuteASA()`

`PEOE_VSA1()`

`PEOE_VSA10()`

`PEOE_VSA11()`

`PEOE_VSA12()`

`PEOE_VSA13()`

`PEOE_VSA14()`

`PEOE_VSA2()`

`PEOE_VSA3()`

`PEOE_VSA4()`

`PEOE_VSA5()`

`PEOE_VSA6()`

`PEOE_VSA7()`

`PEOE_VSA8()`

`PEOE_VSA9()`

`SMR_VSA1()`

`SMR_VSA10()`

`SMR_VSA2()`

`SMR_VSA3()`

`SMR_VSA4()`

`SMR_VSA5()`

`SMR_VSA6()`

`SMR_VSA7()`

`SMR_VSA8()`

`SMR_VSA9()`

`SlogP_VSA1()`

`SlogP_VSA10()`

`SlogP_VSA11()`

`SlogP_VSA12()`

`SlogP_VSA2()`

`SlogP_VSA3()`

`SlogP_VSA4()`

`SlogP_VSA5()`

`SlogP_VSA6()`

`SlogP_VSA7()`

`SlogP_VSA8()`

`SlogP_VSA9()`

`TPSA()`

`pyLabuteASA()`

`pyPEOE_VSA_()`

`pySMR_VSA_()`

`pySlogP_VSA_()`

- rdkit.Chem.PandasTools module
`AddMoleculeColumnToFrame()`

`AddMurckoToFrame()`

`AlignMol()`

`AlignToScaffold()`

`ChangeMoleculeRendering()`

`FrameToGridImage()`

`InstallPandasTools()`

`LoadSDF()`

`PrintAsImageString()`

`RGroupDecompositionToFrame()`

`RemoveSaltsFromFrame()`

`RenderImagesInAllDataFrames()`

`SaveSMILESFromFrame()`

`SaveXlsxFromFrame()`

`TestCase`

`UninstallPandasTools()`

`WriteSDF()`

- rdkit.Chem.PeriodicTable module
- rdkit.Chem.PropertyMol module
- rdkit.Chem.PyMol module
`MolViewer`

`MolViewer.AddPharmacophore()`

`MolViewer.DeleteAll()`

`MolViewer.DeleteAllExcept()`

`MolViewer.DisplayCollisions()`

`MolViewer.DisplayHBonds()`

`MolViewer.DisplayObject()`

`MolViewer.GetAtomCoords()`

`MolViewer.GetPNG()`

`MolViewer.GetSelectedAtoms()`

`MolViewer.HideAll()`

`MolViewer.HideObject()`

`MolViewer.HighlightAtoms()`

`MolViewer.InitializePyMol()`

`MolViewer.LoadFile()`

`MolViewer.Redraw()`

`MolViewer.SaveFile()`

`MolViewer.SelectAtoms()`

`MolViewer.SelectProteinNeighborhood()`

`MolViewer.SetDisplayStyle()`

`MolViewer.SetDisplayUpdate()`

`MolViewer.ShowMol()`

`MolViewer.Zoom()`

- rdkit.Chem.QED module
- rdkit.Chem.Randomize module
- rdkit.Chem.Recap module
`RecapDecompose()`

`RecapHierarchyNode`

`TestCase`

`TestCase.test1()`

`TestCase.test2()`

`TestCase.test3()`

`TestCase.testAmideRxn()`

`TestCase.testAmineRxn()`

`TestCase.testAromCAromCRxn()`

`TestCase.testAromNAliphCRxn()`

`TestCase.testAromNAromCRxn()`

`TestCase.testEsterRxn()`

`TestCase.testEtherRxn()`

`TestCase.testLactamNAliphCRxn()`

`TestCase.testMinFragmentSize()`

`TestCase.testOlefinRxn()`

`TestCase.testSFNetIssue1801871()`

`TestCase.testSFNetIssue1804418()`

`TestCase.testSFNetIssue1881803()`

`TestCase.testSulfonamideRxn()`

`TestCase.testUreaRxn()`

- rdkit.Chem.ReducedGraphs module
- rdkit.Chem.RegistrationHash module
- rdkit.Chem.SATIS module
- rdkit.Chem.SaltRemover module
- rdkit.Chem.ShowMols module
- rdkit.Chem.SpacialScore module
- rdkit.Chem.TemplateAlign module
- rdkit.Chem.TorsionFingerprints module
- rdkit.Chem.inchi module
- rdkit.Chem.rdAbbreviations module
- rdkit.Chem.rdChemicalFeatures module
- rdkit.Chem.rdChemReactions module
`CartesianProductStrategy`

`ChemicalReaction`

`ChemicalReaction.AddAgentTemplate()`

`ChemicalReaction.AddProductTemplate()`

`ChemicalReaction.AddReactantTemplate()`

`ChemicalReaction.AddRecursiveQueriesToReaction()`

`ChemicalReaction.ClearComputedProps()`

`ChemicalReaction.ClearProp()`

`ChemicalReaction.GetAgentTemplate()`

`ChemicalReaction.GetAgents()`

`ChemicalReaction.GetBoolProp()`

`ChemicalReaction.GetDoubleProp()`

`ChemicalReaction.GetIntProp()`

`ChemicalReaction.GetNumAgentTemplates()`

`ChemicalReaction.GetNumProductTemplates()`

`ChemicalReaction.GetNumReactantTemplates()`

`ChemicalReaction.GetProductTemplate()`

`ChemicalReaction.GetProducts()`

`ChemicalReaction.GetProp()`

`ChemicalReaction.GetPropNames()`

`ChemicalReaction.GetPropsAsDict()`

`ChemicalReaction.GetReactantTemplate()`

`ChemicalReaction.GetReactants()`

`ChemicalReaction.GetReactingAtoms()`

`ChemicalReaction.GetSubstructParams()`

`ChemicalReaction.GetUnsignedProp()`

`ChemicalReaction.HasProp()`

`ChemicalReaction.Initialize()`

`ChemicalReaction.IsInitialized()`

`ChemicalReaction.IsMoleculeAgent()`

`ChemicalReaction.IsMoleculeProduct()`

`ChemicalReaction.IsMoleculeReactant()`

`ChemicalReaction.RemoveAgentTemplates()`

`ChemicalReaction.RemoveUnmappedProductTemplates()`

`ChemicalReaction.RemoveUnmappedReactantTemplates()`

`ChemicalReaction.RunReactant()`

`ChemicalReaction.RunReactantInPlace()`

`ChemicalReaction.RunReactants()`

`ChemicalReaction.SetBoolProp()`

`ChemicalReaction.SetDoubleProp()`

`ChemicalReaction.SetIntProp()`

`ChemicalReaction.SetProp()`

`ChemicalReaction.SetUnsignedProp()`

`ChemicalReaction.ToBinary()`

`ChemicalReaction.Validate()`

`Compute2DCoordsForReaction()`

`CreateDifferenceFingerprintForReaction()`

`CreateStructuralFingerprintForReaction()`

`EnumerateLibrary`

`EnumerateLibraryBase`

`EnumerateLibraryBase.GetEnumerator()`

`EnumerateLibraryBase.GetPosition()`

`EnumerateLibraryBase.GetReaction()`

`EnumerateLibraryBase.GetState()`

`EnumerateLibraryBase.InitFromString()`

`EnumerateLibraryBase.ResetState()`

`EnumerateLibraryBase.Serialize()`

`EnumerateLibraryBase.SetState()`

`EnumerateLibraryBase.next()`

`EnumerateLibraryBase.nextSmiles()`

`EnumerateLibraryCanSerialize()`

`EnumerationParams`

`EnumerationStrategyBase`

`EvenSamplePairsStrategy`

`FingerprintType`

`GetChemDrawRxnAdjustParams()`

`GetDefaultAdjustParams()`

`HasAgentTemplateSubstructMatch()`

`HasProductTemplateSubstructMatch()`

`HasReactantTemplateSubstructMatch()`

`HasReactionAtomMapping()`

`HasReactionSubstructMatch()`

`IsReactionTemplateMoleculeAgent()`

`MatchOnlyAtRgroupsAdjustParams()`

`MrvBlockIsReaction()`

`MrvFileIsReaction()`

`PreprocessReaction()`

`RandomSampleAllBBsStrategy`

`RandomSampleStrategy`

`ReactionFingerprintParams`

`ReactionFromMolecule()`

`ReactionFromMrvBlock()`

`ReactionFromMrvFile()`

`ReactionFromPNGFile()`

`ReactionFromPNGString()`

`ReactionFromRxnBlock()`

`ReactionFromRxnFile()`

`ReactionFromSmarts()`

`ReactionFromSmiles()`

`ReactionMetadataToPNGFile()`

`ReactionMetadataToPNGString()`

`ReactionToCXSmarts()`

`ReactionToCXSmiles()`

`ReactionToMolecule()`

`ReactionToMrvBlock()`

`ReactionToMrvFile()`

`ReactionToRxnBlock()`

`ReactionToSmarts()`

`ReactionToSmiles()`

`ReactionToV3KRxnBlock()`

`ReactionsFromCDXMLBlock()`

`ReactionsFromCDXMLFile()`

`ReduceProductToSideChains()`

`RemoveMappingNumbersFromReactions()`

`SanitizeFlags`

`SanitizeRxn()`

`SanitizeRxnAsMols()`

`UpdateProductsStereochemistry()`

`VectMolVect`

- rdkit.Chem.rdchem module
`AddMolSubstanceGroup()`

`Atom`

`Atom.ClearProp()`

`Atom.ClearPropertyCache()`

`Atom.DescribeQuery()`

`Atom.GetAtomMapNum()`

`Atom.GetAtomicNum()`

`Atom.GetBonds()`

`Atom.GetBoolProp()`

`Atom.GetChiralTag()`

`Atom.GetDegree()`

`Atom.GetDoubleProp()`

`Atom.GetExplicitBitVectProp()`

`Atom.GetExplicitValence()`

`Atom.GetFormalCharge()`

`Atom.GetHybridization()`

`Atom.GetIdx()`

`Atom.GetImplicitValence()`

`Atom.GetIntProp()`

`Atom.GetIsAromatic()`

`Atom.GetIsotope()`

`Atom.GetMass()`

`Atom.GetMonomerInfo()`

`Atom.GetNeighbors()`

`Atom.GetNoImplicit()`

`Atom.GetNumExplicitHs()`

`Atom.GetNumImplicitHs()`

`Atom.GetNumRadicalElectrons()`

`Atom.GetOwningMol()`

`Atom.GetPDBResidueInfo()`

`Atom.GetProp()`

`Atom.GetPropNames()`

`Atom.GetPropsAsDict()`

`Atom.GetQueryType()`

`Atom.GetSmarts()`

`Atom.GetSymbol()`

`Atom.GetTotalDegree()`

`Atom.GetTotalNumHs()`

`Atom.GetTotalValence()`

`Atom.GetUnsignedProp()`

`Atom.GetValence()`

`Atom.HasOwningMol()`

`Atom.HasProp()`

`Atom.HasQuery()`

`Atom.HasValenceViolation()`

`Atom.InvertChirality()`

`Atom.IsInRing()`

`Atom.IsInRingSize()`

`Atom.Match()`

`Atom.NOATOM`

`Atom.NeedsUpdatePropertyCache()`

`Atom.SetAtomMapNum()`

`Atom.SetAtomicNum()`

`Atom.SetBoolProp()`

`Atom.SetChiralTag()`

`Atom.SetDoubleProp()`

`Atom.SetExplicitBitVectProp()`

`Atom.SetFormalCharge()`

`Atom.SetHybridization()`

`Atom.SetIntProp()`

`Atom.SetIsAromatic()`

`Atom.SetIsotope()`

`Atom.SetMonomerInfo()`

`Atom.SetNoImplicit()`

`Atom.SetNumExplicitHs()`

`Atom.SetNumRadicalElectrons()`

`Atom.SetPDBResidueInfo()`

`Atom.SetProp()`

`Atom.SetUnsignedProp()`

`Atom.UpdatePropertyCache()`

`AtomCoordsMatcher`

`AtomKekulizeException`

`AtomMonomerInfo`

`AtomMonomerType`

`AtomPDBResidueInfo`

`AtomPDBResidueInfo.GetAltLoc()`

`AtomPDBResidueInfo.GetChainId()`

`AtomPDBResidueInfo.GetInsertionCode()`

`AtomPDBResidueInfo.GetIsHeteroAtom()`

`AtomPDBResidueInfo.GetOccupancy()`

`AtomPDBResidueInfo.GetResidueName()`

`AtomPDBResidueInfo.GetResidueNumber()`

`AtomPDBResidueInfo.GetSecondaryStructure()`

`AtomPDBResidueInfo.GetSegmentNumber()`

`AtomPDBResidueInfo.GetSerialNumber()`

`AtomPDBResidueInfo.GetTempFactor()`

`AtomPDBResidueInfo.SetAltLoc()`

`AtomPDBResidueInfo.SetChainId()`

`AtomPDBResidueInfo.SetInsertionCode()`

`AtomPDBResidueInfo.SetIsHeteroAtom()`

`AtomPDBResidueInfo.SetOccupancy()`

`AtomPDBResidueInfo.SetResidueName()`

`AtomPDBResidueInfo.SetResidueNumber()`

`AtomPDBResidueInfo.SetSecondaryStructure()`

`AtomPDBResidueInfo.SetSegmentNumber()`

`AtomPDBResidueInfo.SetSerialNumber()`

`AtomPDBResidueInfo.SetTempFactor()`

`AtomSanitizeException`

`AtomValenceException`

`Bond`

`Bond.ClearProp()`

`Bond.DescribeQuery()`

`Bond.GetBeginAtom()`

`Bond.GetBeginAtomIdx()`

`Bond.GetBondDir()`

`Bond.GetBondType()`

`Bond.GetBondTypeAsDouble()`

`Bond.GetBoolProp()`

`Bond.GetDoubleProp()`

`Bond.GetEndAtom()`

`Bond.GetEndAtomIdx()`

`Bond.GetIdx()`

`Bond.GetIntProp()`

`Bond.GetIsAromatic()`

`Bond.GetIsConjugated()`

`Bond.GetOtherAtom()`

`Bond.GetOtherAtomIdx()`

`Bond.GetOwningMol()`

`Bond.GetProp()`

`Bond.GetPropNames()`

`Bond.GetPropsAsDict()`

`Bond.GetSmarts()`

`Bond.GetStereo()`

`Bond.GetStereoAtoms()`

`Bond.GetUnsignedProp()`

`Bond.GetValenceContrib()`

`Bond.HasOwningMol()`

`Bond.HasProp()`

`Bond.HasQuery()`

`Bond.InvertChirality()`

`Bond.IsInRing()`

`Bond.IsInRingSize()`

`Bond.Match()`

`Bond.SetBondDir()`

`Bond.SetBondType()`

`Bond.SetBoolProp()`

`Bond.SetDoubleProp()`

`Bond.SetIntProp()`

`Bond.SetIsAromatic()`

`Bond.SetIsConjugated()`

`Bond.SetProp()`

`Bond.SetStereo()`

`Bond.SetStereoAtoms()`

`Bond.SetUnsignedProp()`

`BondDir`

`BondStereo`

`BondType`

`BondType.AROMATIC`

`BondType.DATIVE`

`BondType.DATIVEL`

`BondType.DATIVEONE`

`BondType.DATIVER`

`BondType.DOUBLE`

`BondType.FIVEANDAHALF`

`BondType.FOURANDAHALF`

`BondType.HEXTUPLE`

`BondType.HYDROGEN`

`BondType.IONIC`

`BondType.ONEANDAHALF`

`BondType.OTHER`

`BondType.QUADRUPLE`

`BondType.QUINTUPLE`

`BondType.SINGLE`

`BondType.THREEANDAHALF`

`BondType.THREECENTER`

`BondType.TRIPLE`

`BondType.TWOANDAHALF`

`BondType.UNSPECIFIED`

`BondType.ZERO`

`BondType.names`

`BondType.values`

`ChiralType`

`ClearMolSubstanceGroups()`

`CompositeQueryType`

`Conformer`

`Conformer.ClearComputedProps()`

`Conformer.ClearProp()`

`Conformer.GetAtomPosition()`

`Conformer.GetBoolProp()`

`Conformer.GetDoubleProp()`

`Conformer.GetId()`

`Conformer.GetIntProp()`

`Conformer.GetNumAtoms()`

`Conformer.GetOwningMol()`

`Conformer.GetPositions()`

`Conformer.GetProp()`

`Conformer.GetPropNames()`

`Conformer.GetPropsAsDict()`

`Conformer.GetUnsignedProp()`

`Conformer.HasOwningMol()`

`Conformer.HasProp()`

`Conformer.Is3D()`

`Conformer.Set3D()`

`Conformer.SetAtomPosition()`

`Conformer.SetBoolProp()`

`Conformer.SetDoubleProp()`

`Conformer.SetId()`

`Conformer.SetIntProp()`

`Conformer.SetPositions()`

`Conformer.SetProp()`

`Conformer.SetUnsignedProp()`

`CreateMolDataSubstanceGroup()`

`CreateMolSubstanceGroup()`

`CreateStereoGroup()`

`EditableMol`

`FixedMolSizeMolBundle`

`ForwardStereoGroupIds()`

`GetAtomAlias()`

`GetAtomRLabel()`

`GetAtomValue()`

`GetDefaultPickleProperties()`

`GetMolSubstanceGroupWithIdx()`

`GetMolSubstanceGroups()`

`GetNumPiElectrons()`

`GetPeriodicTable()`

`GetSupplementalSmilesLabel()`

`HybridizationType`

`KekulizeException`

`Mol`

`Mol.AddConformer()`

`Mol.ClearComputedProps()`

`Mol.ClearProp()`

`Mol.ClearPropertyCache()`

`Mol.Debug()`

`Mol.GetAromaticAtoms()`

`Mol.GetAtomWithIdx()`

`Mol.GetAtoms()`

`Mol.GetAtomsMatchingQuery()`

`Mol.GetBondBetweenAtoms()`

`Mol.GetBondWithIdx()`

`Mol.GetBonds()`

`Mol.GetBoolProp()`

`Mol.GetConformer()`

`Mol.GetConformers()`

`Mol.GetDoubleProp()`

`Mol.GetIntProp()`

`Mol.GetNumAtoms()`

`Mol.GetNumBonds()`

`Mol.GetNumConformers()`

`Mol.GetNumHeavyAtoms()`

`Mol.GetProp()`

`Mol.GetPropNames()`

`Mol.GetPropsAsDict()`

`Mol.GetRingInfo()`

`Mol.GetStereoGroups()`

`Mol.GetSubstructMatch()`

`Mol.GetSubstructMatches()`

`Mol.GetUnsignedProp()`

`Mol.HasProp()`

`Mol.HasQuery()`

`Mol.HasSubstructMatch()`

`Mol.NeedsUpdatePropertyCache()`

`Mol.RemoveAllConformers()`

`Mol.RemoveConformer()`

`Mol.SetBoolProp()`

`Mol.SetDoubleProp()`

`Mol.SetIntProp()`

`Mol.SetProp()`

`Mol.SetUnsignedProp()`

`Mol.ToBinary()`

`Mol.UpdatePropertyCache()`

`MolBundle`

`MolBundleCanSerialize()`

`MolSanitizeException`

`PeriodicTable`

`PeriodicTable.GetAbundanceForIsotope()`

`PeriodicTable.GetAtomicNumber()`

`PeriodicTable.GetAtomicWeight()`

`PeriodicTable.GetDefaultValence()`

`PeriodicTable.GetElementName()`

`PeriodicTable.GetElementSymbol()`

`PeriodicTable.GetMassForIsotope()`

`PeriodicTable.GetMaxAtomicNumber()`

`PeriodicTable.GetMostCommonIsotope()`

`PeriodicTable.GetMostCommonIsotopeMass()`

`PeriodicTable.GetNOuterElecs()`

`PeriodicTable.GetRb0()`

`PeriodicTable.GetRcovalent()`

`PeriodicTable.GetRow()`

`PeriodicTable.GetRvdw()`

`PeriodicTable.GetValenceList()`

`PropertyPickleOptions`

`PropertyPickleOptions.AllProps`

`PropertyPickleOptions.AtomProps`

`PropertyPickleOptions.BondProps`

`PropertyPickleOptions.ComputedProps`

`PropertyPickleOptions.CoordsAsDouble`

`PropertyPickleOptions.MolProps`

`PropertyPickleOptions.NoConformers`

`PropertyPickleOptions.NoProps`

`PropertyPickleOptions.PrivateProps`

`PropertyPickleOptions.QueryAtomData`

`PropertyPickleOptions.names`

`PropertyPickleOptions.values`

`QueryAtom`

`QueryBond`

`RWMol`

`ResonanceFlags`

`ResonanceMolSupplier`

`ResonanceMolSupplier.Enumerate()`

`ResonanceMolSupplier.GetAtomConjGrpIdx()`

`ResonanceMolSupplier.GetBondConjGrpIdx()`

`ResonanceMolSupplier.GetIsEnumerated()`

`ResonanceMolSupplier.GetNumConjGrps()`

`ResonanceMolSupplier.GetProgressCallback()`

`ResonanceMolSupplier.GetSubstructMatch()`

`ResonanceMolSupplier.GetSubstructMatches()`

`ResonanceMolSupplier.SetNumThreads()`

`ResonanceMolSupplier.SetProgressCallback()`

`ResonanceMolSupplier.WasCanceled()`

`ResonanceMolSupplier.atEnd()`

`ResonanceMolSupplier.reset()`

`ResonanceMolSupplierCallback`

`RingInfo`

`RingInfo.AddRing()`

`RingInfo.AreAtomsInSameRing()`

`RingInfo.AreAtomsInSameRingOfSize()`

`RingInfo.AreBondsInSameRing()`

`RingInfo.AreBondsInSameRingOfSize()`

`RingInfo.AreRingFamiliesInitialized()`

`RingInfo.AreRingsFused()`

`RingInfo.AtomMembers()`

`RingInfo.AtomRingFamilies()`

`RingInfo.AtomRingSizes()`

`RingInfo.AtomRings()`

`RingInfo.BondMembers()`

`RingInfo.BondRingFamilies()`

`RingInfo.BondRingSizes()`

`RingInfo.BondRings()`

`RingInfo.IsAtomInRingOfSize()`

`RingInfo.IsBondInRingOfSize()`

`RingInfo.IsRingFused()`

`RingInfo.MinAtomRingSize()`

`RingInfo.MinBondRingSize()`

`RingInfo.NumAtomRings()`

`RingInfo.NumBondRings()`

`RingInfo.NumFusedBonds()`

`RingInfo.NumRelevantCycles()`

`RingInfo.NumRingFamilies()`

`RingInfo.NumRings()`

`SetAtomAlias()`

`SetAtomRLabel()`

`SetAtomValue()`

`SetDefaultPickleProperties()`

`SetSupplementalSmilesLabel()`

`StereoDescriptor`

`StereoGroup`

`StereoGroupType`

`StereoGroup_vect`

`StereoInfo`

`StereoSpecified`

`StereoType`

`SubstanceGroup`

`SubstanceGroup.AddAtomWithBookmark()`

`SubstanceGroup.AddAtomWithIdx()`

`SubstanceGroup.AddAttachPoint()`

`SubstanceGroup.AddBondWithBookmark()`

`SubstanceGroup.AddBondWithIdx()`

`SubstanceGroup.AddBracket()`

`SubstanceGroup.AddCState()`

`SubstanceGroup.AddParentAtomWithBookmark()`

`SubstanceGroup.AddParentAtomWithIdx()`

`SubstanceGroup.ClearAttachPoints()`

`SubstanceGroup.ClearBrackets()`

`SubstanceGroup.ClearCStates()`

`SubstanceGroup.ClearProp()`

`SubstanceGroup.GetAtoms()`

`SubstanceGroup.GetAttachPoints()`

`SubstanceGroup.GetBonds()`

`SubstanceGroup.GetBoolProp()`

`SubstanceGroup.GetBrackets()`

`SubstanceGroup.GetCStates()`

`SubstanceGroup.GetDoubleProp()`

`SubstanceGroup.GetIndexInMol()`

`SubstanceGroup.GetIntProp()`

`SubstanceGroup.GetOwningMol()`

`SubstanceGroup.GetParentAtoms()`

`SubstanceGroup.GetProp()`

`SubstanceGroup.GetPropNames()`

`SubstanceGroup.GetPropsAsDict()`

`SubstanceGroup.GetStringVectProp()`

`SubstanceGroup.GetUnsignedProp()`

`SubstanceGroup.GetUnsignedVectProp()`

`SubstanceGroup.HasProp()`

`SubstanceGroup.SetAtoms()`

`SubstanceGroup.SetBonds()`

`SubstanceGroup.SetBoolProp()`

`SubstanceGroup.SetDoubleProp()`

`SubstanceGroup.SetIntProp()`

`SubstanceGroup.SetParentAtoms()`

`SubstanceGroup.SetProp()`

`SubstanceGroup.SetUnsignedProp()`

`SubstanceGroupAttach`

`SubstanceGroupCState`

`SubstanceGroup_VECT`

`SubstructMatchParameters`

`SubstructMatchParameters.aromaticMatchesConjugated`

`SubstructMatchParameters.aromaticMatchesSingleOrDouble`

`SubstructMatchParameters.atomProperties`

`SubstructMatchParameters.bondProperties`

`SubstructMatchParameters.extraAtomCheckOverridesDefaultCheck`

`SubstructMatchParameters.extraBondCheckOverridesDefaultCheck`

`SubstructMatchParameters.maxMatches`

`SubstructMatchParameters.maxRecursiveMatches`

`SubstructMatchParameters.numThreads`

`SubstructMatchParameters.recursionPossible`

`SubstructMatchParameters.setExtraAtomCheckFunc()`

`SubstructMatchParameters.setExtraBondCheckFunc()`

`SubstructMatchParameters.setExtraFinalCheck()`

`SubstructMatchParameters.specifiedStereoQueryMatchesUnspecified`

`SubstructMatchParameters.uniquify`

`SubstructMatchParameters.useChirality`

`SubstructMatchParameters.useEnhancedStereo`

`SubstructMatchParameters.useGenericMatchers`

`SubstructMatchParameters.useQueryQueryMatches`

`ValenceType`

`tossit()`

- rdkit.Chem.rdCIPLabeler module
- rdkit.Chem.rdCoordGen module
`AddCoords()`

`CoordGenParams`

`CoordGenParams.SetCoordMap()`

`CoordGenParams.SetTemplateMol()`

`CoordGenParams.coordgenScaling`

`CoordGenParams.dbg_useConstrained`

`CoordGenParams.dbg_useFixed`

`CoordGenParams.minimizerPrecision`

`CoordGenParams.sketcherBestPrecision`

`CoordGenParams.sketcherCoarsePrecision`

`CoordGenParams.sketcherQuickPrecision`

`CoordGenParams.sketcherStandardPrecision`

`CoordGenParams.templateFileDir`

`CoordGenParams.treatNonterminalBondsToMetalAsZOBs`

`SetDefaultTemplateFileDir()`

- rdkit.Chem.rdDepictor module
`AddRingSystemTemplates()`

`Compute2DCoords()`

`Compute2DCoordsMimicDistmat()`

`ConstrainedDepictionParams`

`GenerateDepictionMatching2DStructure()`

`GenerateDepictionMatching3DStructure()`

`GetPreferCoordGen()`

`IsCoordGenSupportAvailable()`

`LoadDefaultRingSystemTemplates()`

`NormalizeDepiction()`

`SetPreferCoordGen()`

`SetRingSystemTemplates()`

`StraightenDepiction()`

`UsingCoordGen`

- rdkit.Chem.rdDeprotect module
- rdkit.Chem.rdDetermineBonds module
- rdkit.Chem.rdDistGeom module
`ETDG()`

`ETDGv2()`

`ETKDG()`

`ETKDGv2()`

`ETKDGv3()`

`EmbedFailureCauses`

`EmbedFailureCauses.BAD_DOUBLE_BOND_STEREO`

`EmbedFailureCauses.CHECK_CHIRAL_CENTERS`

`EmbedFailureCauses.CHECK_CHIRAL_CENTERS2`

`EmbedFailureCauses.CHECK_TETRAHEDRAL_CENTERS`

`EmbedFailureCauses.ETK_MINIMIZATION`

`EmbedFailureCauses.EXCEEDED_TIMEOUT`

`EmbedFailureCauses.FINAL_CENTER_IN_VOLUME`

`EmbedFailureCauses.FINAL_CHIRAL_BOUNDS`

`EmbedFailureCauses.FIRST_MINIMIZATION`

`EmbedFailureCauses.INITIAL_COORDS`

`EmbedFailureCauses.LINEAR_DOUBLE_BOND`

`EmbedFailureCauses.MINIMIZE_FOURTH_DIMENSION`

`EmbedFailureCauses.names`

`EmbedFailureCauses.values`

`EmbedMolecule()`

`EmbedMultipleConfs()`

`EmbedParameters`

`EmbedParameters.ETversion`

`EmbedParameters.GetFailureCounts()`

`EmbedParameters.SetBoundsMat()`

`EmbedParameters.SetCPCI()`

`EmbedParameters.SetCoordMap()`

`EmbedParameters.basinThresh`

`EmbedParameters.boundsMatForceScaling`

`EmbedParameters.boxSizeMult`

`EmbedParameters.clearConfs`

`EmbedParameters.embedFragmentsSeparately`

`EmbedParameters.enableSequentialRandomSeeds`

`EmbedParameters.enforceChirality`

`EmbedParameters.forceTransAmides`

`EmbedParameters.ignoreSmoothingFailures`

`EmbedParameters.maxIterations`

`EmbedParameters.numThreads`

`EmbedParameters.numZeroFail`

`EmbedParameters.onlyHeavyAtomsForRMS`

`EmbedParameters.optimizerForceTol`

`EmbedParameters.pruneRmsThresh`

`EmbedParameters.randNegEig`

`EmbedParameters.randomSeed`

`EmbedParameters.symmetrizeConjugatedTerminalGroupsForPruning`

`EmbedParameters.timeout`

`EmbedParameters.trackFailures`

`EmbedParameters.useBasicKnowledge`

`EmbedParameters.useExpTorsionAnglePrefs`

`EmbedParameters.useMacrocycle14config`

`EmbedParameters.useMacrocycleTorsions`

`EmbedParameters.useRandomCoords`

`EmbedParameters.useSmallRingTorsions`

`EmbedParameters.useSymmetryForPruning`

`EmbedParameters.verbose`

`EmbedParametersToJSON()`

`GetExperimentalTorsions()`

`GetMoleculeBoundsMatrix()`

`KDG()`

`srETKDGv3()`

- rdkit.Chem.rdEHTTools module
- rdkit.Chem.rdEnumerateStereoisomers module
- rdkit.Chem.rdfiltercatalog module
`ExclusionList`

`FilterCatalog`

`FilterCatalogCanSerialize()`

`FilterCatalogEntry`

`FilterCatalogEntry.ClearProp()`

`FilterCatalogEntry.GetDescription()`

`FilterCatalogEntry.GetFilterMatches()`

`FilterCatalogEntry.GetProp()`

`FilterCatalogEntry.GetPropList()`

`FilterCatalogEntry.HasFilterMatch()`

`FilterCatalogEntry.IsValid()`

`FilterCatalogEntry.Serialize()`

`FilterCatalogEntry.SetDescription()`

`FilterCatalogEntry.SetProp()`

`FilterCatalogEntryList`

`FilterCatalogListOfEntryList`

`FilterCatalogParams`

`FilterCatalogParams.AddCatalog()`

`FilterCatalogParams.FilterCatalogs`

`FilterCatalogParams.FilterCatalogs.ALL`

`FilterCatalogParams.FilterCatalogs.BRENK`

`FilterCatalogParams.FilterCatalogs.CHEMBL`

`FilterCatalogParams.FilterCatalogs.CHEMBL_BMS`

`FilterCatalogParams.FilterCatalogs.CHEMBL_Dundee`

`FilterCatalogParams.FilterCatalogs.CHEMBL_Glaxo`

`FilterCatalogParams.FilterCatalogs.CHEMBL_Inpharmatica`

`FilterCatalogParams.FilterCatalogs.CHEMBL_LINT`

`FilterCatalogParams.FilterCatalogs.CHEMBL_MLSMR`

`FilterCatalogParams.FilterCatalogs.CHEMBL_SureChEMBL`

`FilterCatalogParams.FilterCatalogs.NIH`

`FilterCatalogParams.FilterCatalogs.PAINS`

`FilterCatalogParams.FilterCatalogs.PAINS_A`

`FilterCatalogParams.FilterCatalogs.PAINS_B`

`FilterCatalogParams.FilterCatalogs.PAINS_C`

`FilterCatalogParams.FilterCatalogs.ZINC`

`FilterCatalogParams.FilterCatalogs.names`

`FilterCatalogParams.FilterCatalogs.values`

`FilterHierarchyMatcher`

`FilterMatch`

`FilterMatcherBase`

`GetFlattenedFunctionalGroupHierarchy()`

`GetFunctionalGroupHierarchy()`

`IntPair`

`MolList`

`PythonFilterMatcher`

`RunFilterCatalog()`

`SmartsMatcher`

`VectFilterMatch`

- rdkit.Chem.rdFingerprintGenerator module
`AdditionalOutput`

`AdditionalOutput.AllocateAtomCounts()`

`AdditionalOutput.AllocateAtomToBits()`

`AdditionalOutput.AllocateAtomsPerBit()`

`AdditionalOutput.AllocateBitInfoMap()`

`AdditionalOutput.AllocateBitPaths()`

`AdditionalOutput.CollectAtomCounts()`

`AdditionalOutput.CollectAtomToBits()`

`AdditionalOutput.CollectAtomsPerBit()`

`AdditionalOutput.CollectBitInfoMap()`

`AdditionalOutput.CollectBitPaths()`

`AdditionalOutput.GetAtomCounts()`

`AdditionalOutput.GetAtomToBits()`

`AdditionalOutput.GetAtomsPerBit()`

`AdditionalOutput.GetBitInfoMap()`

`AdditionalOutput.GetBitPaths()`

`AtomInvariantsGenerator`

`AtomPairFingerprintOptions`

`BondInvariantsGenerator`

`FPType`

`FingerprintGenerator32`

`FingerprintGenerator32.GetCountFingerprint()`

`FingerprintGenerator32.GetCountFingerprintAsNumPy()`

`FingerprintGenerator32.GetCountFingerprints()`

`FingerprintGenerator32.GetFingerprint()`

`FingerprintGenerator32.GetFingerprintAsNumPy()`

`FingerprintGenerator32.GetFingerprints()`

`FingerprintGenerator32.GetInfoString()`

`FingerprintGenerator32.GetOptions()`

`FingerprintGenerator32.GetSparseCountFingerprint()`

`FingerprintGenerator32.GetSparseCountFingerprints()`

`FingerprintGenerator32.GetSparseFingerprint()`

`FingerprintGenerator32.GetSparseFingerprints()`

`FingerprintGenerator32.ToJSON()`

`FingerprintGenerator64`

`FingerprintGenerator64.GetCountFingerprint()`

`FingerprintGenerator64.GetCountFingerprintAsNumPy()`

`FingerprintGenerator64.GetCountFingerprints()`

`FingerprintGenerator64.GetFingerprint()`

`FingerprintGenerator64.GetFingerprintAsNumPy()`

`FingerprintGenerator64.GetFingerprints()`

`FingerprintGenerator64.GetInfoString()`

`FingerprintGenerator64.GetOptions()`

`FingerprintGenerator64.GetSparseCountFingerprint()`

`FingerprintGenerator64.GetSparseCountFingerprints()`

`FingerprintGenerator64.GetSparseFingerprint()`

`FingerprintGenerator64.GetSparseFingerprints()`

`FingerprintGenerator64.ToJSON()`

`FingerprintGeneratorFromJSON()`

`FingerprintOptions`

`GetAtomPairAtomInvGen()`

`GetAtomPairGenerator()`

`GetCountFPs()`

`GetFPs()`

`GetMorganAtomInvGen()`

`GetMorganBondInvGen()`

`GetMorganFeatureAtomInvGen()`

`GetMorganGenerator()`

`GetRDKitAtomInvGen()`

`GetRDKitFPGenerator()`

`GetSparseCountFPs()`

`GetSparseFPs()`

`GetTopologicalTorsionGenerator()`

`MorganFingerprintOptions`

`RDKitFingerprintOptions`

`TopologicalTorsionFingerprintOptions`

- rdkit.Chem.rdFMCS module
`AtomCompare`

`BondCompare`

`FindMCS()`

`MCSAcceptance`

`MCSAtomCompare`

`MCSAtomCompareParameters`

`MCSBondCompare`

`MCSBondCompareParameters`

`MCSFinalMatchCheck`

`MCSParameters`

`MCSParameters.AtomCompareParameters`

`MCSParameters.AtomTyper`

`MCSParameters.BondCompareParameters`

`MCSParameters.BondTyper`

`MCSParameters.FinalMatchChecker`

`MCSParameters.InitialSeed`

`MCSParameters.MaximizeBonds`

`MCSParameters.ProgressCallback`

`MCSParameters.ShouldAcceptMCS`

`MCSParameters.StoreAll`

`MCSParameters.Threshold`

`MCSParameters.Timeout`

`MCSParameters.Verbose`

`MCSProgress`

`MCSProgressData`

`MCSResult`

`RingCompare`

- rdkit.Chem.rdForceFieldHelpers module
`CreateEmptyForceFieldForMol()`

`GetUFFAngleBendParams()`

`GetUFFBondStretchParams()`

`GetUFFInversionParams()`

`GetUFFTorsionParams()`

`GetUFFVdWParams()`

`MMFFGetMoleculeForceField()`

`MMFFGetMoleculeProperties()`

`MMFFHasAllMoleculeParams()`

`MMFFOptimizeMolecule()`

`MMFFOptimizeMoleculeConfs()`

`MMFFSanitizeMolecule()`

`OptimizeMolecule()`

`OptimizeMoleculeConfs()`

`UFFGetMoleculeForceField()`

`UFFHasAllMoleculeParams()`

`UFFOptimizeMolecule()`

`UFFOptimizeMoleculeConfs()`

- rdkit.Chem.rdfragcatalog module
`FragCatGenerator`

`FragCatParams`

`FragCatalog`

`FragCatalog.GetBitDescription()`

`FragCatalog.GetBitDiscrims()`

`FragCatalog.GetBitEntryId()`

`FragCatalog.GetBitFuncGroupIds()`

`FragCatalog.GetBitOrder()`

`FragCatalog.GetCatalogParams()`

`FragCatalog.GetEntryBitId()`

`FragCatalog.GetEntryDescription()`

`FragCatalog.GetEntryDownIds()`

`FragCatalog.GetEntryFuncGroupIds()`

`FragCatalog.GetEntryOrder()`

`FragCatalog.GetFPLength()`

`FragCatalog.GetNumEntries()`

`FragCatalog.Serialize()`

`FragFPGenerator`

- rdkit.Chem.rdFreeSASA module
- rdkit.Chem.rdGeneralizedSubstruct module
- rdkit.Chem.rdinchi module
- rdkit.Chem.rdMHFPFingerprint module
`MHFPEncoder`

`MHFPEncoder.CreateShinglingFromMol()`

`MHFPEncoder.CreateShinglingFromSmiles()`

`MHFPEncoder.Distance()`

`MHFPEncoder.EncodeMol()`

`MHFPEncoder.EncodeMolsBulk()`

`MHFPEncoder.EncodeSECFPMol()`

`MHFPEncoder.EncodeSECFPMolsBulk()`

`MHFPEncoder.EncodeSECFPSmiles()`

`MHFPEncoder.EncodeSECFPSmilesBulk()`

`MHFPEncoder.EncodeSmiles()`

`MHFPEncoder.EncodeSmilesBulk()`

`MHFPEncoder.FromArray()`

`MHFPEncoder.FromStringArray()`

- rdkit.Chem.rdMIF module
- rdkit.Chem.rdMMPA module
- rdkit.Chem.rdMolAlign module
- rdkit.Chem.rdMolCatalog module
- rdkit.Chem.rdMolChemicalFeatures module
`BuildFeatureFactory()`

`BuildFeatureFactoryFromString()`

`GetAtomMatch()`

`MolChemicalFeature`

`MolChemicalFeature.ClearCache()`

`MolChemicalFeature.GetActiveConformer()`

`MolChemicalFeature.GetAtomIds()`

`MolChemicalFeature.GetFactory()`

`MolChemicalFeature.GetFamily()`

`MolChemicalFeature.GetId()`

`MolChemicalFeature.GetMol()`

`MolChemicalFeature.GetPos()`

`MolChemicalFeature.GetType()`

`MolChemicalFeature.SetActiveConformer()`

`MolChemicalFeatureFactory`

- rdkit.Chem.rdMolDescriptors module
`AtomPairsParameters`

`BCUT2D()`

`CalcAUTOCORR2D()`

`CalcAUTOCORR3D()`

`CalcAsphericity()`

`CalcChi0n()`

`CalcChi0v()`

`CalcChi1n()`

`CalcChi1v()`

`CalcChi2n()`

`CalcChi2v()`

`CalcChi3n()`

`CalcChi3v()`

`CalcChi4n()`

`CalcChi4v()`

`CalcChiNn()`

`CalcChiNv()`

`CalcCoulombMat()`

`CalcCrippenDescriptors()`

`CalcEEMcharges()`

`CalcEccentricity()`

`CalcExactMolWt()`

`CalcFractionCSP3()`

`CalcGETAWAY()`

`CalcHallKierAlpha()`

`CalcInertialShapeFactor()`

`CalcKappa1()`

`CalcKappa2()`

`CalcKappa3()`

`CalcLabuteASA()`

`CalcMORSE()`

`CalcMolFormula()`

`CalcNPR1()`

`CalcNPR2()`

`CalcNumAliphaticCarbocycles()`

`CalcNumAliphaticHeterocycles()`

`CalcNumAliphaticRings()`

`CalcNumAmideBonds()`

`CalcNumAromaticCarbocycles()`

`CalcNumAromaticHeterocycles()`

`CalcNumAromaticRings()`

`CalcNumAtomStereoCenters()`

`CalcNumAtoms()`

`CalcNumBridgeheadAtoms()`

`CalcNumHBA()`

`CalcNumHBD()`

`CalcNumHeavyAtoms()`

`CalcNumHeteroatoms()`

`CalcNumHeterocycles()`

`CalcNumLipinskiHBA()`

`CalcNumLipinskiHBD()`

`CalcNumRings()`

`CalcNumRotatableBonds()`

`CalcNumSaturatedCarbocycles()`

`CalcNumSaturatedHeterocycles()`

`CalcNumSaturatedRings()`

`CalcNumSpiroAtoms()`

`CalcNumUnspecifiedAtomStereoCenters()`

`CalcOxidationNumbers()`

`CalcPBF()`

`CalcPMI1()`

`CalcPMI2()`

`CalcPMI3()`

`CalcPhi()`

`CalcRDF()`

`CalcRadiusOfGyration()`

`CalcSpherocityIndex()`

`CalcTPSA()`

`CalcWHIM()`

`CustomProp_VSA_()`

`DoubleCubicLatticeVolume`

`DoubleCubicLatticeVolume.GetAtomSurfaceArea()`

`DoubleCubicLatticeVolume.GetAtomVolume()`

`DoubleCubicLatticeVolume.GetCompactness()`

`DoubleCubicLatticeVolume.GetPackingDensity()`

`DoubleCubicLatticeVolume.GetPartialSurfaceArea()`

`DoubleCubicLatticeVolume.GetPartialVolume()`

`DoubleCubicLatticeVolume.GetPolarSurfaceArea()`

`DoubleCubicLatticeVolume.GetPolarVolume()`

`DoubleCubicLatticeVolume.GetSurfaceArea()`

`DoubleCubicLatticeVolume.GetSurfacePoints()`

`DoubleCubicLatticeVolume.GetVDWVolume()`

`DoubleCubicLatticeVolume.GetVolume()`

`GetAtomFeatures()`

`GetAtomPairAtomCode()`

`GetAtomPairCode()`

`GetAtomPairFingerprint()`

`GetConnectivityInvariants()`

`GetFeatureInvariants()`

`GetHashedAtomPairFingerprint()`

`GetHashedAtomPairFingerprintAsBitVect()`

`GetHashedMorganFingerprint()`

`GetHashedTopologicalTorsionFingerprint()`

`GetHashedTopologicalTorsionFingerprintAsBitVect()`

`GetMACCSKeysFingerprint()`

`GetMorganFingerprint()`

`GetMorganFingerprintAsBitVect()`

`GetTopologicalTorsionFingerprint()`

`GetUSR()`

`GetUSRCAT()`

`GetUSRDistributions()`

`GetUSRDistributionsFromPoints()`

`GetUSRFromDistributions()`

`GetUSRScore()`

`MQNs_()`

`MakePropertyRangeQuery()`

`NumRotatableBondsOptions`

`PEOE_VSA_()`

`Properties`

`PropertyFunctor`

`PropertyRangeQuery`

`PythonPropertyFunctor`

`SMR_VSA_()`

`SlogP_VSA_()`

- rdkit.Chem.rdMolEnumerator module
- rdkit.Chem.rdmolfiles module
`AddMetadataToPNGFile()`

`AddMetadataToPNGString()`

`AtomFromSmarts()`

`AtomFromSmiles()`

`BondFromSmarts()`

`BondFromSmiles()`

`CDXMLFormat`

`CDXMLParserParams`

`CXSmilesFields`

`CXSmilesFields.CX_ALL`

`CXSmilesFields.CX_ALL_BUT_COORDS`

`CXSmilesFields.CX_ATOM_LABELS`

`CXSmilesFields.CX_ATOM_PROPS`

`CXSmilesFields.CX_BOND_ATROPISOMER`

`CXSmilesFields.CX_BOND_CFG`

`CXSmilesFields.CX_COORDINATE_BONDS`

`CXSmilesFields.CX_COORDS`

`CXSmilesFields.CX_ENHANCEDSTEREO`

`CXSmilesFields.CX_LINKNODES`

`CXSmilesFields.CX_MOLFILE_VALUES`

`CXSmilesFields.CX_NONE`

`CXSmilesFields.CX_POLYMER`

`CXSmilesFields.CX_RADICALS`

`CXSmilesFields.CX_SGROUPS`

`CXSmilesFields.CX_ZERO_BONDS`

`CXSmilesFields.names`

`CXSmilesFields.values`

`CanonicalRankAtoms()`

`CanonicalRankAtomsInFragment()`

`CanonicalizeEnhancedStereo()`

`CreateAtomBoolPropertyList()`

`CreateAtomDoublePropertyList()`

`CreateAtomIntPropertyList()`

`CreateAtomStringPropertyList()`

`CreateBondBoolPropertyList()`

`CreateBondDoublePropertyList()`

`CreateBondIntPropertyList()`

`CreateBondStringPropertyList()`

`ForwardSDMolSupplier`

`HasChemDrawCDXSupport()`

`MaeMolSupplier`

`MaeWriter`

`MetadataFromPNGFile()`

`MetadataFromPNGString()`

`MolFragmentToCXSmarts()`

`MolFragmentToCXSmiles()`

`MolFragmentToSmarts()`

`MolFragmentToSmiles()`

`MolFromFASTA()`

`MolFromHELM()`

`MolFromMol2Block()`

`MolFromMol2File()`

`MolFromMolBlock()`

`MolFromMolFile()`

`MolFromMrvBlock()`

`MolFromMrvFile()`

`MolFromPDBBlock()`

`MolFromPDBFile()`

`MolFromPNGFile()`

`MolFromPNGString()`

`MolFromRDKitSVG()`

`MolFromSCSRBlock()`

`MolFromSCSRFile()`

`MolFromSCSRParams`

`MolFromSequence()`

`MolFromSmarts()`

`MolFromSmiles()`

`MolFromTPLBlock()`

`MolFromTPLFile()`

`MolFromXYZBlock()`

`MolFromXYZFile()`

`MolMetadataToPNGFile()`

`MolMetadataToPNGString()`

`MolToCMLBlock()`

`MolToCMLFile()`

`MolToCXSmarts()`

`MolToCXSmiles()`

`MolToFASTA()`

`MolToHELM()`

`MolToMolBlock()`

`MolToMolFile()`

`MolToMrvBlock()`

`MolToMrvFile()`

`MolToPDBBlock()`

`MolToPDBFile()`

`MolToRandomSmilesVect()`

`MolToSequence()`

`MolToSmarts()`

`MolToSmiles()`

`MolToTPLBlock()`

`MolToTPLFile()`

`MolToV2KMolBlock()`

`MolToV3KMolBlock()`

`MolToV3KMolFile()`

`MolToXYZBlock()`

`MolToXYZFile()`

`MolWriterParams`

`MolsFromCDXML()`

`MolsFromCDXMLFile()`

`MolsFromPNGFile()`

`MolsFromPNGString()`

`MultithreadedSDMolSupplier`

`MultithreadedSmilesMolSupplier`

`PDBWriter`

`PNGMetadataParams`

`RestoreBondDirOption`

`SCSRBaseHbondOptions`

`SCSRTemplateNames`

`SDMolSupplier`

`SDWriter`

`SmartsParserParams`

`SmilesMolSupplier`

`SmilesMolSupplierFromText()`

`SmilesParserParams`

`SmilesWriteParams`

`SmilesWriteParams.allBondsExplicit`

`SmilesWriteParams.allHsExplicit`

`SmilesWriteParams.canonical`

`SmilesWriteParams.cleanStereo`

`SmilesWriteParams.doIsomericSmiles`

`SmilesWriteParams.doKekule`

`SmilesWriteParams.doRandom`

`SmilesWriteParams.ignoreAtomMapNumbers`

`SmilesWriteParams.includeDativeBonds`

`SmilesWriteParams.rootedAtAtom`

`SmilesWriter`

`TDTMolSupplier`

`TDTWriter`

- rdkit.Chem.rdMolHash module
`HashFunction`

`HashFunction.AnonymousGraph`

`HashFunction.ArthorSubstructureOrder`

`HashFunction.AtomBondCounts`

`HashFunction.CanonicalSmiles`

`HashFunction.DegreeVector`

`HashFunction.ElementGraph`

`HashFunction.ExtendedMurcko`

`HashFunction.HetAtomProtomer`

`HashFunction.HetAtomProtomerv2`

`HashFunction.HetAtomTautomer`

`HashFunction.HetAtomTautomerv2`

`HashFunction.Mesomer`

`HashFunction.MolFormula`

`HashFunction.MurckoScaffold`

`HashFunction.NetCharge`

`HashFunction.RedoxPair`

`HashFunction.Regioisomer`

`HashFunction.SmallWorldIndexBR`

`HashFunction.SmallWorldIndexBRL`

`HashFunction.names`

`HashFunction.values`

`MolHash()`

- rdkit.Chem.rdMolInterchange module
- rdkit.Chem.rdmolops module
`AddHs()`

`AddHsParameters`

`AddRecursiveQuery()`

`AddStereoAnnotations()`

`AddWavyBondsForStereoAny()`

`AdjustQueryParameters`

`AdjustQueryParameters.NoAdjustments()`

`AdjustQueryParameters.adjustConjugatedFiveRings`

`AdjustQueryParameters.adjustDegree`

`AdjustQueryParameters.adjustDegreeFlags`

`AdjustQueryParameters.adjustHeavyDegree`

`AdjustQueryParameters.adjustHeavyDegreeFlags`

`AdjustQueryParameters.adjustRingChain`

`AdjustQueryParameters.adjustRingChainFlags`

`AdjustQueryParameters.adjustRingCount`

`AdjustQueryParameters.adjustRingCountFlags`

`AdjustQueryParameters.adjustSingleBondsBetweenAromaticAtoms`

`AdjustQueryParameters.adjustSingleBondsToDegreeOneNeighbors`

`AdjustQueryParameters.aromatizeIfPossible`

`AdjustQueryParameters.makeAtomsGeneric`

`AdjustQueryParameters.makeAtomsGenericFlags`

`AdjustQueryParameters.makeBondsGeneric`

`AdjustQueryParameters.makeBondsGenericFlags`

`AdjustQueryParameters.makeDummiesQueries`

`AdjustQueryParameters.setMDLFiveRingAromaticity`

`AdjustQueryParameters.useStereoCareForBonds`

`AdjustQueryProperties()`

`AdjustQueryPropertiesWithGenericGroups()`

`AdjustQueryWhichFlags`

`AdjustQueryWhichFlags.ADJUST_IGNOREALL`

`AdjustQueryWhichFlags.ADJUST_IGNORECHAINS`

`AdjustQueryWhichFlags.ADJUST_IGNOREDUMMIES`

`AdjustQueryWhichFlags.ADJUST_IGNOREMAPPED`

`AdjustQueryWhichFlags.ADJUST_IGNORENONDUMMIES`

`AdjustQueryWhichFlags.ADJUST_IGNORENONE`

`AdjustQueryWhichFlags.ADJUST_IGNORERINGS`

`AdjustQueryWhichFlags.names`

`AdjustQueryWhichFlags.values`

`AromaticityModel`

`AssignAtomChiralTagsFromMolParity()`

`AssignAtomChiralTagsFromStructure()`

`AssignChiralTypesFromBondDirs()`

`AssignRadicals()`

`AssignStereochemistry()`

`AssignStereochemistryFrom3D()`

`AtomHasConjugatedBond()`

`BondWedgingParameters`

`BoolVector`

`CanonicalizeStereoGroups()`

`Cleanup()`

`CleanupAtropisomers()`

`CleanupChirality()`

`CleanupOrganometallics()`

`CleanupStereoGroups()`

`CollapseAttachmentPoints()`

`CombineMols()`

`ComputeAtomCIPRanks()`

`ConvertGenericQueriesToSubstanceGroups()`

`CopyMolSubset()`

`CountAtomElec()`

`DativeBondsToHaptic()`

`DeleteSubstructs()`

`DetectBondStereoChemistry()`

`DetectBondStereochemistry()`

`DetectChemistryProblems()`

`ExpandAttachmentPoints()`

`FastFindRings()`

`FindAllPathsOfLengthN()`

`FindAllSubgraphsOfLengthMToN()`

`FindAllSubgraphsOfLengthN()`

`FindAtomEnvironmentOfRadiusN()`

`FindMesoCenters()`

`FindPotentialStereo()`

`FindPotentialStereoBonds()`

`FindRingFamilies()`

`FindUniqueSubgraphsOfLengthN()`

`FragmentOnBRICSBonds()`

`FragmentOnBonds()`

`FragmentOnSomeBonds()`

`Get3DDistanceMatrix()`

`GetAdjacencyMatrix()`

`GetAllowNontetrahedralChirality()`

`GetDistanceMatrix()`

`GetFormalCharge()`

`GetMolFrags()`

`GetMostSubstitutedCoreMatch()`

`GetSSSR()`

`GetShortestPath()`

`GetSymmSSSR()`

`GetUseLegacyStereoPerception()`

`HapticBondsToDative()`

`HasQueryHs()`

`Kekulize()`

`KekulizeIfPossible()`

`LayeredFingerprint()`

`MergeQueryHs()`

`MolAddRecursiveQueries()`

`MolzipLabel`

`MolzipParams`

`MurckoDecompose()`

`NeedsHs()`

`ParseMolQueryDefFile()`

`PathToSubmol()`

`PatternFingerprint()`

`RDKFingerprint()`

`ReapplyMolBlockWedging()`

`RemoveAllHs()`

`RemoveHs()`

`RemoveHsParameters`

`RemoveHsParameters.removeAndTrackIsotopes`

`RemoveHsParameters.removeDefiningBondStereo`

`RemoveHsParameters.removeDegreeZero`

`RemoveHsParameters.removeDummyNeighbors`

`RemoveHsParameters.removeHigherDegrees`

`RemoveHsParameters.removeHydrides`

`RemoveHsParameters.removeInSGroups`

`RemoveHsParameters.removeIsotopes`

`RemoveHsParameters.removeMapped`

`RemoveHsParameters.removeNonimplicit`

`RemoveHsParameters.removeNontetrahedralNeighbors`

`RemoveHsParameters.removeOnlyHNeighbors`

`RemoveHsParameters.removeWithQuery`

`RemoveHsParameters.removeWithWedgedBond`

`RemoveHsParameters.showWarnings`

`RemoveHsParameters.updateExplicitCount`

`RemoveNonExplicit3DChirality()`

`RemoveStereochemistry()`

`RenumberAtoms()`

`ReplaceCore()`

`ReplaceSidechains()`

`ReplaceSubstructs()`

`SanitizeFlags`

`SanitizeFlags.SANITIZE_ADJUSTHS`

`SanitizeFlags.SANITIZE_ALL`

`SanitizeFlags.SANITIZE_CLEANUP`

`SanitizeFlags.SANITIZE_CLEANUPATROPISOMERS`

`SanitizeFlags.SANITIZE_CLEANUPCHIRALITY`

`SanitizeFlags.SANITIZE_CLEANUP_ORGANOMETALLICS`

`SanitizeFlags.SANITIZE_FINDRADICALS`

`SanitizeFlags.SANITIZE_KEKULIZE`

`SanitizeFlags.SANITIZE_NONE`

`SanitizeFlags.SANITIZE_PROPERTIES`

`SanitizeFlags.SANITIZE_SETAROMATICITY`

`SanitizeFlags.SANITIZE_SETCONJUGATION`

`SanitizeFlags.SANITIZE_SETHYBRIDIZATION`

`SanitizeFlags.SANITIZE_SYMMRINGS`

`SanitizeFlags.names`

`SanitizeFlags.values`

`SanitizeMol()`

`SetAllowNontetrahedralChirality()`

`SetAromaticity()`

`SetBondStereoFromDirections()`

`SetConjugation()`

`SetDoubleBondNeighborDirections()`

`SetGenericQueriesFromProperties()`

`SetHybridization()`

`SetTerminalAtomCoords()`

`SetUseLegacyStereoPerception()`

`SimplifyEnhancedStereo()`

`SortMatchesByDegreeOfCoreSubstitution()`

`SplitMolByPDBChainId()`

`SplitMolByPDBResidues()`

`StereoBondThresholds`

`StereoGroupAbsOptions`

`SubsetInfo`

`SubsetMethod`

`SubsetOptions`

`TranslateChiralFlagToStereoGroups()`

`UIntUIntMap`

`UnfoldedRDKFingerprintCountBased()`

`WedgeBond()`

`WedgeMolBonds()`

`map_indexing_suite_UIntUIntMap_entry`

`molzip()`

`molzipFragments()`

- rdkit.Chem.rdMolProcessing module
- rdkit.Chem.rdMolTransforms module
`CanonicalizeConformer()`

`CanonicalizeMol()`

`ComputeCanonicalTransform()`

`ComputeCentroid()`

`ComputePrincipalAxesAndMoments()`

`ComputePrincipalAxesAndMomentsFromGyrationMatrix()`

`GetAngleDeg()`

`GetAngleRad()`

`GetBondLength()`

`GetDihedralDeg()`

`GetDihedralRad()`

`SetAngleDeg()`

`SetAngleRad()`

`SetBondLength()`

`SetDihedralDeg()`

`SetDihedralRad()`

`TransformConformer()`

- rdkit.Chem.rdPartialCharges module
- rdkit.Chem.rdqueries module
`AAtomQueryAtom()`

`AHAtomQueryAtom()`

`AtomNumEqualsQueryAtom()`

`AtomNumGreaterQueryAtom()`

`AtomNumLessQueryAtom()`

`ExplicitDegreeEqualsQueryAtom()`

`ExplicitDegreeGreaterQueryAtom()`

`ExplicitDegreeLessQueryAtom()`

`ExplicitValenceEqualsQueryAtom()`

`ExplicitValenceGreaterQueryAtom()`

`ExplicitValenceLessQueryAtom()`

`FormalChargeEqualsQueryAtom()`

`FormalChargeGreaterQueryAtom()`

`FormalChargeLessQueryAtom()`

`HCountEqualsQueryAtom()`

`HCountGreaterQueryAtom()`

`HCountLessQueryAtom()`

`HasBitVectPropWithValueQueryAtom()`

`HasBoolPropWithValueQueryAtom()`

`HasBoolPropWithValueQueryBond()`

`HasChiralTagQueryAtom()`

`HasDoublePropWithValueQueryAtom()`

`HasDoublePropWithValueQueryBond()`

`HasIntPropWithValueQueryAtom()`

`HasIntPropWithValueQueryBond()`

`HasPropQueryAtom()`

`HasPropQueryBond()`

`HasStringPropWithValueQueryAtom()`

`HasStringPropWithValueQueryBond()`

`HybridizationEqualsQueryAtom()`

`HybridizationGreaterQueryAtom()`

`HybridizationLessQueryAtom()`

`InNRingsEqualsQueryAtom()`

`InNRingsGreaterQueryAtom()`

`InNRingsLessQueryAtom()`

`IsAliphaticQueryAtom()`

`IsAromaticQueryAtom()`

`IsBridgeheadQueryAtom()`

`IsInRingQueryAtom()`

`IsUnsaturatedQueryAtom()`

`IsotopeEqualsQueryAtom()`

`IsotopeGreaterQueryAtom()`

`IsotopeLessQueryAtom()`

`MAtomQueryAtom()`

`MHAtomQueryAtom()`

`MassEqualsQueryAtom()`

`MassGreaterQueryAtom()`

`MassLessQueryAtom()`

`MinRingSizeEqualsQueryAtom()`

`MinRingSizeGreaterQueryAtom()`

`MinRingSizeLessQueryAtom()`

`MissingChiralTagQueryAtom()`

`NonHydrogenDegreeEqualsQueryAtom()`

`NonHydrogenDegreeGreaterQueryAtom()`

`NonHydrogenDegreeLessQueryAtom()`

`NumAliphaticHeteroatomNeighborsEqualsQueryAtom()`

`NumAliphaticHeteroatomNeighborsGreaterQueryAtom()`

`NumAliphaticHeteroatomNeighborsLessQueryAtom()`

`NumHeteroatomNeighborsEqualsQueryAtom()`

`NumHeteroatomNeighborsGreaterQueryAtom()`

`NumHeteroatomNeighborsLessQueryAtom()`

`NumRadicalElectronsEqualsQueryAtom()`

`NumRadicalElectronsGreaterQueryAtom()`

`NumRadicalElectronsLessQueryAtom()`

`QAtomQueryAtom()`

`QHAtomQueryAtom()`

`ReplaceAtomWithQueryAtom()`

`RingBondCountEqualsQueryAtom()`

`RingBondCountGreaterQueryAtom()`

`RingBondCountLessQueryAtom()`

`TotalDegreeEqualsQueryAtom()`

`TotalDegreeGreaterQueryAtom()`

`TotalDegreeLessQueryAtom()`

`TotalValenceEqualsQueryAtom()`

`TotalValenceGreaterQueryAtom()`

`TotalValenceLessQueryAtom()`

`XAtomQueryAtom()`

`XHAtomQueryAtom()`

- rdkit.Chem.rdRascalMCES module
`FindMCES()`

`RascalButinaCluster()`

`RascalCluster()`

`RascalClusterOptions`

`RascalOptions`

`RascalOptions.allBestMCESs`

`RascalOptions.completeAromaticRings`

`RascalOptions.completeSmallestRings`

`RascalOptions.equivalentAtoms`

`RascalOptions.exactConnectionsMatch`

`RascalOptions.ignoreAtomAromaticity`

`RascalOptions.ignoreBondOrders`

`RascalOptions.maxBestMCESs`

`RascalOptions.maxBondMatchPairs`

`RascalOptions.maxFragSeparation`

`RascalOptions.minCliqueSize`

`RascalOptions.minFragSize`

`RascalOptions.returnEmptyMCES`

`RascalOptions.ringMatchesRingOnly`

`RascalOptions.similarityThreshold`

`RascalOptions.singleLargestFrag`

`RascalOptions.timeout`

`RascalResult`

- rdkit.Chem.rdReducedGraphs module
- rdkit.Chem.rdRGroupDecomposition module
`RGroupCoreAlignment`

`RGroupDecompose()`

`RGroupDecomposition`

`RGroupDecompositionParameters`

`RGroupDecompositionParameters.alignment`

`RGroupDecompositionParameters.allowMultipleCoresInSameMol`

`RGroupDecompositionParameters.allowMultipleRGroupsOnUnlabelled`

`RGroupDecompositionParameters.allowNonTerminalRGroups`

`RGroupDecompositionParameters.chunkSize`

`RGroupDecompositionParameters.doEnumeration`

`RGroupDecompositionParameters.doTautomers`

`RGroupDecompositionParameters.gaMaximumOperations`

`RGroupDecompositionParameters.gaNumberOperationsWithoutImprovement`

`RGroupDecompositionParameters.gaNumberRuns`

`RGroupDecompositionParameters.gaParallelRuns`

`RGroupDecompositionParameters.gaPopulationSize`

`RGroupDecompositionParameters.gaRandomSeed`

`RGroupDecompositionParameters.includeTargetMolInResults`

`RGroupDecompositionParameters.labels`

`RGroupDecompositionParameters.matchingStrategy`

`RGroupDecompositionParameters.onlyMatchAtRGroups`

`RGroupDecompositionParameters.removeAllHydrogenRGroups`

`RGroupDecompositionParameters.removeAllHydrogenRGroupsAndLabels`

`RGroupDecompositionParameters.removeHydrogensPostMatch`

`RGroupDecompositionParameters.rgroupLabelling`

`RGroupDecompositionParameters.scoreMethod`

`RGroupDecompositionParameters.substructMatchParams`

`RGroupDecompositionParameters.timeout`

`RGroupLabelling`

`RGroupLabels`

`RGroupMatching`

`RGroupScore`

`RelabelMappedDummies()`

- rdkit.Chem.rdShapeAlign module
- rdkit.Chem.rdShapeHelpers module
- rdkit.Chem.rdSLNParse module
- rdkit.Chem.rdSubstructLibrary module
`AddPatterns()`

`CachedMolHolder`

`CachedSmilesMolHolder`

`CachedTrustedSmilesMolHolder`

`FPHolderBase`

`KeyFromPropHolder`

`KeyHolderBase`

`MolHolder`

`MolHolderBase`

`PatternHolder`

`SubstructLibrary`

`SubstructLibrary.AddMol()`

`SubstructLibrary.CountMatches()`

`SubstructLibrary.GetFpHolder()`

`SubstructLibrary.GetKeyHolder()`

`SubstructLibrary.GetMatches()`

`SubstructLibrary.GetMol()`

`SubstructLibrary.GetMolHolder()`

`SubstructLibrary.GetSearchOrder()`

`SubstructLibrary.HasMatch()`

`SubstructLibrary.InitFromStream()`

`SubstructLibrary.Serialize()`

`SubstructLibrary.SetSearchOrder()`

`SubstructLibrary.ToStream()`

`SubstructLibraryCanSerialize()`

`TautomerPatternHolder`

- rdkit.Chem.rdSynthonSpaceSearch module
`ConvertTextToDBFile()`

`FormattedIntegerString()`

`SubstructureResult`

`SynthonSpace`

`SynthonSpace.BuildSynthonFingerprints()`

`SynthonSpace.FingerprintSearch()`

`SynthonSpace.FingerprintSearchIncremental()`

`SynthonSpace.GetNumProducts()`

`SynthonSpace.GetNumReactions()`

`SynthonSpace.GetSynthonFingerprintType()`

`SynthonSpace.RascalSearch()`

`SynthonSpace.RascalSearchIncremental()`

`SynthonSpace.ReadDBFile()`

`SynthonSpace.ReadTextFile()`

`SynthonSpace.SubstructureSearch()`

`SynthonSpace.SubstructureSearchIncremental()`

`SynthonSpace.Summarise()`

`SynthonSpace.WriteDBFile()`

`SynthonSpace.WriteEnumeratedFile()`

`SynthonSpaceSearchParams`

`SynthonSpaceSearchParams.approxSimilarityAdjuster`

`SynthonSpaceSearchParams.buildHits`

`SynthonSpaceSearchParams.fragSimilarityAdjuster`

`SynthonSpaceSearchParams.hitStart`

`SynthonSpaceSearchParams.maxHitChiralAtoms`

`SynthonSpaceSearchParams.maxHitHeavyAtoms`

`SynthonSpaceSearchParams.maxHitMolWt`

`SynthonSpaceSearchParams.maxHits`

`SynthonSpaceSearchParams.maxNumFrags`

`SynthonSpaceSearchParams.minHitChiralAtoms`

`SynthonSpaceSearchParams.minHitHeavyAtoms`

`SynthonSpaceSearchParams.minHitMolWt`

`SynthonSpaceSearchParams.numRandomSweeps`

`SynthonSpaceSearchParams.numThreads`

`SynthonSpaceSearchParams.randomSample`

`SynthonSpaceSearchParams.randomSeed`

`SynthonSpaceSearchParams.similarityCutoff`

`SynthonSpaceSearchParams.timeOut`

`SynthonSpaceSearchParams.toTryChunkSize`

- rdkit.Chem.rdTautomerQuery module
`PatternFingerprintTautomerTarget()`

`TautomerQuery`

`TautomerQuery.GetModifiedAtoms()`

`TautomerQuery.GetModifiedBonds()`

`TautomerQuery.GetSubstructMatch()`

`TautomerQuery.GetSubstructMatches()`

`TautomerQuery.GetSubstructMatchesWithTautomers()`

`TautomerQuery.GetTautomers()`

`TautomerQuery.GetTemplateMolecule()`

`TautomerQuery.IsSubstructOf()`

`TautomerQuery.PatternFingerprintTemplate()`

`TautomerQuery.ToBinary()`

`TautomerQueryCanSerialize()`

- rdkit.Chem.rdtrajectory module

- Module contents

- Subpackages
- rdkit.DataManip package
- rdkit.DataStructs package
- Submodules
- rdkit.DataStructs.BitEnsemble module
- rdkit.DataStructs.BitEnsembleDb module
- rdkit.DataStructs.BitUtils module
- rdkit.DataStructs.LazySignature module
- rdkit.DataStructs.TopNContainer module
- rdkit.DataStructs.VectCollection module
`VectCollection`

`VectCollection.AddVect()`

`VectCollection.DetachVectsMatchingBit()`

`VectCollection.DetachVectsNotMatchingBit()`

`VectCollection.GetBit()`

`VectCollection.GetChildren()`

`VectCollection.GetNumBits()`

`VectCollection.GetOnBits()`

`VectCollection.GetOrVect()`

`VectCollection.NumChildren()`

`VectCollection.Reset()`

`VectCollection.Uniquify()`

`VectCollection.orVect`

- rdkit.DataStructs.cDataStructs module
`AllBitSimilarity()`

`AllProbeBitsMatch()`

`AsymmetricSimilarity()`

`AsymmetricSimilarityNeighbors()`

`AsymmetricSimilarityNeighbors_sparse()`

`BitVectToBinaryText()`

`BitVectToFPSText()`

`BitVectToText()`

`BraunBlanquetSimilarity()`

`BraunBlanquetSimilarityNeighbors()`

`BraunBlanquetSimilarityNeighbors_sparse()`

`BulkAllBitSimilarity()`

`BulkAsymmetricSimilarity()`

`BulkBraunBlanquetSimilarity()`

`BulkCosineSimilarity()`

`BulkDiceSimilarity()`

`BulkKulczynskiSimilarity()`

`BulkMcConnaugheySimilarity()`

`BulkOnBitSimilarity()`

`BulkRogotGoldbergSimilarity()`

`BulkRusselSimilarity()`

`BulkSokalSimilarity()`

`BulkTanimotoSimilarity()`

`BulkTverskySimilarity()`

`ComputeL1Norm()`

`ConvertToExplicit()`

`ConvertToNumpyArray()`

`CosineSimilarity()`

`CosineSimilarityNeighbors()`

`CosineSimilarityNeighbors_sparse()`

`CreateFromBinaryText()`

`CreateFromBitString()`

`CreateFromFPSText()`

`DiceSimilarity()`

`DiceSimilarityNeighbors()`

`DiceSimilarityNeighbors_sparse()`

`DiscreteValueType`

`DiscreteValueVect`

`ExplicitBitVect`

`ExplicitBitVect.FromBase64()`

`ExplicitBitVect.GetBit()`

`ExplicitBitVect.GetNumBits()`

`ExplicitBitVect.GetNumOffBits()`

`ExplicitBitVect.GetNumOnBits()`

`ExplicitBitVect.GetOnBits()`

`ExplicitBitVect.SetBit()`

`ExplicitBitVect.SetBitsFromList()`

`ExplicitBitVect.ToBase64()`

`ExplicitBitVect.ToBinary()`

`ExplicitBitVect.ToBitString()`

`ExplicitBitVect.ToList()`

`ExplicitBitVect.UnSetBit()`

`ExplicitBitVect.UnSetBitsFromList()`

`FPBReader`

`FoldFingerprint()`

`InitFromDaylightString()`

`IntSparseIntVect`

`KulczynskiSimilarity()`

`KulczynskiSimilarityNeighbors()`

`KulczynskiSimilarityNeighbors_sparse()`

`LongSparseIntVect`

`McConnaugheySimilarity()`

`McConnaugheySimilarityNeighbors()`

`McConnaugheySimilarityNeighbors_sparse()`

`MultiFPBReader`

`NumBitsInCommon()`

`OffBitProjSimilarity()`

`OffBitsInCommon()`

`OnBitProjSimilarity()`

`OnBitSimilarity()`

`OnBitsInCommon()`

`RealValueVect`

`RogotGoldbergSimilarity()`

`RogotGoldbergSimilarityNeighbors()`

`RogotGoldbergSimilarityNeighbors_sparse()`

`RusselSimilarity()`

`RusselSimilarityNeighbors()`

`RusselSimilarityNeighbors_sparse()`

`SokalSimilarity()`

`SokalSimilarityNeighbors()`

`SokalSimilarityNeighbors_sparse()`

`SparseBitVect`

`SparseBitVect.FromBase64()`

`SparseBitVect.GetBit()`

`SparseBitVect.GetNumBits()`

`SparseBitVect.GetNumOffBits()`

`SparseBitVect.GetNumOnBits()`

`SparseBitVect.GetOnBits()`

`SparseBitVect.SetBit()`

`SparseBitVect.SetBitsFromList()`

`SparseBitVect.ToBase64()`

`SparseBitVect.ToBinary()`

`SparseBitVect.ToBitString()`

`SparseBitVect.ToList()`

`SparseBitVect.UnSetBit()`

`SparseBitVect.UnSetBitsFromList()`

`TanimotoSimilarity()`

`TanimotoSimilarityNeighbors()`

`TanimotoSimilarityNeighbors_sparse()`

`TverskySimilarity()`

`UIntSparseIntVect`

`ULongSparseIntVect`

- Module contents

- Submodules
- rdkit.Dbase package
- Submodules
- rdkit.Dbase.DbConnection module
`DbConnect`

`DbConnect.AddColumn()`

`DbConnect.AddTable()`

`DbConnect.Commit()`

`DbConnect.GetColumnNames()`

`DbConnect.GetColumnNamesAndTypes()`

`DbConnect.GetColumns()`

`DbConnect.GetCursor()`

`DbConnect.GetData()`

`DbConnect.GetDataCount()`

`DbConnect.GetTableNames()`

`DbConnect.InsertColumnData()`

`DbConnect.InsertData()`

`DbConnect.KillCursor()`

`DbError`

- rdkit.Dbase.DbInfo module
- rdkit.Dbase.DbModule module
- rdkit.Dbase.DbResultSet module
- rdkit.Dbase.DbUtils module
- rdkit.Dbase.StorageUtils module

- rdkit.Dbase.DbConnection module
- Module contents

- Submodules
- rdkit.DistanceGeometry package
- rdkit.ForceField package
- rdkit.ForceField.rdForceField module
`ForceField`

`ForceField.AddDistanceConstraint()`

`ForceField.AddExtraPoint()`

`ForceField.AddFixedPoint()`

`ForceField.CalcEnergy()`

`ForceField.CalcGrad()`

`ForceField.Dimension()`

`ForceField.GetExtraPointPos()`

`ForceField.Initialize()`

`ForceField.MMFFAddAngleConstraint()`

`ForceField.MMFFAddDistanceConstraint()`

`ForceField.MMFFAddPositionConstraint()`

`ForceField.MMFFAddTorsionConstraint()`

`ForceField.Minimize()`

`ForceField.MinimizeTrajectory()`

`ForceField.NumPoints()`

`ForceField.Positions()`

`ForceField.UFFAddAngleConstraint()`

`ForceField.UFFAddDistanceConstraint()`

`ForceField.UFFAddPositionConstraint()`

`ForceField.UFFAddTorsionConstraint()`

`MMFFMolProperties`

`MMFFMolProperties.GetMMFFAngleBendParams()`

`MMFFMolProperties.GetMMFFAtomType()`

`MMFFMolProperties.GetMMFFBondStretchParams()`

`MMFFMolProperties.GetMMFFFormalCharge()`

`MMFFMolProperties.GetMMFFOopBendParams()`

`MMFFMolProperties.GetMMFFPartialCharge()`

`MMFFMolProperties.GetMMFFStretchBendParams()`

`MMFFMolProperties.GetMMFFTorsionParams()`

`MMFFMolProperties.GetMMFFVdWParams()`

`MMFFMolProperties.SetMMFFAngleTerm()`

`MMFFMolProperties.SetMMFFBondTerm()`

`MMFFMolProperties.SetMMFFDielectricConstant()`

`MMFFMolProperties.SetMMFFDielectricModel()`

`MMFFMolProperties.SetMMFFEleTerm()`

`MMFFMolProperties.SetMMFFOopTerm()`

`MMFFMolProperties.SetMMFFStretchBendTerm()`

`MMFFMolProperties.SetMMFFTorsionTerm()`

`MMFFMolProperties.SetMMFFVariant()`

`MMFFMolProperties.SetMMFFVdWTerm()`

`MMFFMolProperties.SetMMFFVerbosity()`

- Module contents

- rdkit.ForceField.rdForceField module
- rdkit.Geometry package
- Submodules
- rdkit.Geometry.rdGeometry module
`ComputeDihedralAngle()`

`ComputeGridCentroid()`

`ComputeSignedDihedralAngle()`

`FindGridTerminalPoints()`

`Point2D`

`Point3D`

`PointND`

`ProtrudeDistance()`

`TanimotoDistance()`

`TverskyIndex()`

`UniformGrid3D()`

`UniformGrid3D_`

`UniformGrid3D_.CompareParams()`

`UniformGrid3D_.GetGridIndex()`

`UniformGrid3D_.GetGridIndices()`

`UniformGrid3D_.GetGridPointIndex()`

`UniformGrid3D_.GetGridPointLoc()`

`UniformGrid3D_.GetNumX()`

`UniformGrid3D_.GetNumY()`

`UniformGrid3D_.GetNumZ()`

`UniformGrid3D_.GetOccupancyVect()`

`UniformGrid3D_.GetOffset()`

`UniformGrid3D_.GetSize()`

`UniformGrid3D_.GetSpacing()`

`UniformGrid3D_.GetVal()`

`UniformGrid3D_.GetValPoint()`

`UniformGrid3D_.SetSphereOccupancy()`

`UniformGrid3D_.SetVal()`

`UniformGrid3D_.SetValPoint()`

`UniformRealValueGrid3D`

`UniformRealValueGrid3D.CompareGrids()`

`UniformRealValueGrid3D.CompareParams()`

`UniformRealValueGrid3D.CompareVectors()`

`UniformRealValueGrid3D.GetGridIndex()`

`UniformRealValueGrid3D.GetGridIndices()`

`UniformRealValueGrid3D.GetGridPointIndex()`

`UniformRealValueGrid3D.GetGridPointLoc()`

`UniformRealValueGrid3D.GetNumX()`

`UniformRealValueGrid3D.GetNumY()`

`UniformRealValueGrid3D.GetNumZ()`

`UniformRealValueGrid3D.GetOccupancyVect()`

`UniformRealValueGrid3D.GetOffset()`

`UniformRealValueGrid3D.GetSize()`

`UniformRealValueGrid3D.GetSpacing()`

`UniformRealValueGrid3D.GetVal()`

`UniformRealValueGrid3D.GetValPoint()`

`UniformRealValueGrid3D.SetVal()`

`UniformRealValueGrid3D.SetValPoint()`

`WriteGridToFile()`

- rdkit.Geometry.rdGeometry module
- Module contents

- Submodules
- rdkit.ML package
- Subpackages
- rdkit.ML.Cluster package
- Submodules
- rdkit.ML.Cluster.Butina module
- rdkit.ML.Cluster.ClusterUtils module
- rdkit.ML.Cluster.ClusterVis module
- rdkit.ML.Cluster.Clusters module
`Cluster`

`Cluster.AddChild()`

`Cluster.AddChildren()`

`Cluster.Compare()`

`Cluster.FindSubtree()`

`Cluster.GetChildren()`

`Cluster.GetData()`

`Cluster.GetIndex()`

`Cluster.GetMetric()`

`Cluster.GetName()`

`Cluster.GetPoints()`

`Cluster.GetPointsPositions()`

`Cluster.GetPosition()`

`Cluster.IsTerminal()`

`Cluster.Print()`

`Cluster.RemoveChild()`

`Cluster.SetData()`

`Cluster.SetIndex()`

`Cluster.SetMetric()`

`Cluster.SetName()`

`Cluster.SetPosition()`

`cmp()`

- rdkit.ML.Cluster.Murtagh module
- rdkit.ML.Cluster.Resemblance module
- rdkit.ML.Cluster.Standardize module
- rdkit.ML.Cluster.Clustering module

- Module contents

- Submodules
- rdkit.ML.Data package
- Submodules
- rdkit.ML.Data.DataUtils module
- rdkit.ML.Data.FindQuantBounds module
- rdkit.ML.Data.MLData module
`MLDataSet`

`MLDataSet.AddPoint()`

`MLDataSet.AddPoints()`

`MLDataSet.GetAllData()`

`MLDataSet.GetInputData()`

`MLDataSet.GetNPossibleVals()`

`MLDataSet.GetNPts()`

`MLDataSet.GetNResults()`

`MLDataSet.GetNVars()`

`MLDataSet.GetNamedData()`

`MLDataSet.GetPtNames()`

`MLDataSet.GetQuantBounds()`

`MLDataSet.GetResults()`

`MLDataSet.GetVarNames()`

`MLQuantDataSet`

- rdkit.ML.Data.Quantize module
- rdkit.ML.Data.cQuantize module
- rdkit.ML.Data.SplitData module
- rdkit.ML.Data.Stats module
- rdkit.ML.Data.Transforms module

- Module contents

- Submodules
- rdkit.ML.Descriptors package
- Submodules
- rdkit.ML.Descriptors.CompoundDescriptors module
`CompoundDescriptorCalculator`

`CompoundDescriptorCalculator.BuildAtomDict()`

`CompoundDescriptorCalculator.CalcCompoundDescriptorsForComposition()`

`CompoundDescriptorCalculator.CalcDescriptors()`

`CompoundDescriptorCalculator.CalcDescriptorsForComposition()`

`CompoundDescriptorCalculator.CalcSimpleDescriptorsForComposition()`

`CompoundDescriptorCalculator.DEV()`

`CompoundDescriptorCalculator.GetDescriptorNames()`

`CompoundDescriptorCalculator.MAX()`

`CompoundDescriptorCalculator.MEAN()`

`CompoundDescriptorCalculator.MIN()`

`CompoundDescriptorCalculator.ProcessCompoundList()`

`CompoundDescriptorCalculator.ProcessSimpleList()`

`CompoundDescriptorCalculator.SUM()`

`GetAllDescriptorNames()`

- rdkit.ML.Descriptors.Descriptors module
- rdkit.ML.Descriptors.MoleculeDescriptors module
`MolecularDescriptorCalculator`

`MolecularDescriptorCalculator.CalcDescriptors()`

`MolecularDescriptorCalculator.GetDescriptorFuncs()`

`MolecularDescriptorCalculator.GetDescriptorNames()`

`MolecularDescriptorCalculator.GetDescriptorSummaries()`

`MolecularDescriptorCalculator.GetDescriptorVersions()`

`MolecularDescriptorCalculator.SaveState()`

- rdkit.ML.Descriptors.Parser module

- rdkit.ML.Descriptors.CompoundDescriptors module
- Module contents

- Submodules
- rdkit.ML.InfoTheory package
- rdkit.ML.MLUtils package
- rdkit.ML.SLT package
- rdkit.ML.Scoring package

- rdkit.ML.Cluster package
- Submodules
- Module contents

- Subpackages
- rdkit.Numerics package
- rdkit.SimDivFilters package
- rdkit.VLib package
- Subpackages
- rdkit.VLib.NodeLib package
- Submodules
- rdkit.VLib.NodeLib.DbMolSupply module
- rdkit.VLib.NodeLib.DbPickleSupplier module
- rdkit.VLib.NodeLib.SDSupply module
- rdkit.VLib.NodeLib.SmartsMolFilter module
- rdkit.VLib.NodeLib.SmartsRemover module
- rdkit.VLib.NodeLib.SmilesDupeFilter module
- rdkit.VLib.NodeLib.SmilesOutput module
- rdkit.VLib.NodeLib.SmilesSupply module

- Module contents

- Submodules

- rdkit.VLib.NodeLib package
- Submodules
- Module contents

- Subpackages
- rdkit.utils package

## Submodules¶

- rdkit.rdBase module
`AttachFileToLog()`

`BlockLogs`

`DisableLog()`

`EnableLog()`

`LogDebugMsg()`

`LogErrorMsg()`

`LogInfoMsg()`

`LogMessage()`

`LogStatus()`

`LogToCppStreams()`

`LogToPythonLogger()`

`LogToPythonStderr()`

`LogWarningMsg()`

`MatchTypeVect`

`SeedRandomNumberGenerator()`

`UnsignedLong_Vect`

`VectorOfStringVectors`

`WrapLogs()`

`ostream`

`std_ostream`

`streambuf`

- rdkit.RDConfig module
- rdkit.RDLogger module
- rdkit.RDPaths module
- rdkit.RDRandom module
- rdkit.TestRunner module

## Module contents¶

-
class rdkit.VectIter(
*vect*)¶ Bases:

`object`

## Source: https://www.rdkit.org/docs/source/rdkit.Avalon.html

# rdkit.Avalon package¶

## Submodules¶

- rdkit.Avalon.pyAvalonTools module
`CheckMolecule()`

`CheckMoleculeString()`

`CloseCheckMolFiles()`

`Generate2DCoords()`

`GetAvalonCountFP()`

`GetAvalonFP()`

`GetAvalonFPAsWords()`

`GetCanonSmiles()`

`GetCheckMolLog()`

`InitializeCheckMol()`

`StruChkFlag`

`StruChkFlag.alias_conversion_failed`

`StruChkFlag.atom_check_failed`

`StruChkFlag.atom_clash`

`StruChkFlag.bad_molecule`

`StruChkFlag.dubious_stereo_removed`

`StruChkFlag.either_warning`

`StruChkFlag.fragments_found`

`StruChkFlag.names`

`StruChkFlag.recharged`

`StruChkFlag.size_check_failed`

`StruChkFlag.stereo_error`

`StruChkFlag.stereo_forced_bad`

`StruChkFlag.stereo_transformed`

`StruChkFlag.template_transformed`

`StruChkFlag.transformed`

`StruChkFlag.values`

`StruChkResult`
