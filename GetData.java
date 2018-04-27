//test function starts from here - invalid

function getTestFile(sheet) {

  var

public static Credential authorize() throws IOException {
    // Load client secrets.
    File cfile = new File("certs/cert.json");
    cfile.createNewFile();
    GoogleClientSecrets clientSecrets = GoogleClientSecrets.load(jsonFactory, new InputStreamReader(new FileInputStream(cfile)));

    // Build flow and trigger user authorization request.
    GoogleAuthorizationCodeFlow flow =
            new GoogleAuthorizationCodeFlow.Builder(
                    transport, jsonFactory, clientSecrets, scopes)
                    .setDataStoreFactory(dataStoreFactory)
                    .setAccessType("offline")
                    .build();
    Credential credential = new AuthorizationCodeInstalledApp(flow, new LocalServerReceiver()).authorize("user");
    return credential;
}

public static Sheets getSheetsService() throws IOException {
    Credential credential = authorize();
    return new Sheets.Builder(transport, jsonFactory, credential)
            .setApplicationName("INSERT_YOUR_APPLICATION_NAME")
            .build();
}

public void writeSomething(List<Data> myData) {

    try {
        String id = "INSERT_SHEET_ID";
        String writeRange = "INSERT_SHEET_NAME!A3:E";

        List<List<Object>> writeData = new ArrayList<>();
        for (Data someData: myData) {
            List<Object> dataRow = new ArrayList<>();
            dataRow.add(someData.data1);
            dataRow.add(someData.data2);
            dataRow.add(someData.data3);
            dataRow.add(someData.data4);
            dataRow.add(someData.data5);
            writeData.add(dataRow);
        }

        ValueRange vr = new ValueRange().setValues(writeData).setMajorDimension("ROWS");
        service.spreadsheets().values()
                .update(id, writeRange, vr)
                .setValueInputOption("RAW")
                .execute();
    } catch (Exception e) {
        // handle exception
    }
}
