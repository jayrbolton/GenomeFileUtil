/*

*/
module GenomeFileUtil {

    /* A boolean - 0 for false, 1 for true.
       @range (0, 1)
    */
    typedef int boolean;

    typedef structure {
        string path;
        string shock_id;
        string ftp_url;
    } File;

    typedef mapping<string, string> usermeta;

    /* 
        genome_name - becomes the name of the object
	workspace_name - the name of the workspace it gets saved to.
	source - Source of the file typically something like RefSeq or Ensembl
	taxon_ws_name - where the reference taxons are : ReferenceTaxons
	release - Release or version number of the data 
          per example Ensembl has numbered releases of all their data: Release 31
	generate_ids_if_needed - If field used for feature id is not there, 
          generate ids (default behavior is raising an exception)
        genetic_code - Genetic code of organism. Overwrites determined GC from 
          taxon object
	type - Reference, Representative or User upload

    */
    typedef structure {
        File file;

        string genome_name;
        string workspace_name;

        string source;
        string taxon_wsname;
	string release;
	string generate_ids_if_needed;
	int    genetic_code;
	string type;
	usermeta metadata;

    } GenbankToGenomeParams;

    typedef structure {
        string genome_ref;
    } GenomeSaveResult;

    funcdef genbank_to_genome(GenbankToGenomeParams params)
                returns (GenomeSaveResult result) authentication required;




    typedef structure {
        string genome_ref;
        list <string> ref_path_to_genome;
    } GenomeToGFFParams;

    /* from_cache is 1 if the file already exists and was just returned, 0 if
    the file was generated during this call. */
    typedef structure {
        File gff_file;
        boolean from_cache;
    } GenomeToGFFResult;

    funcdef genome_to_gff(GenomeToGFFParams params)
                returns (GenomeToGFFResult result) authentication required;


};
