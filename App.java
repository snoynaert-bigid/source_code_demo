package com.fabrikam;

import com.azure.core.credential.TokenCredential;
import com.azure.core.http.policy.HttpLogDetailLevel;
import com.azure.core.management.AzureEnvironment;
import com.azure.core.management.Region;
import com.azure.core.management.profile.AzureProfile;
import com.azure.identity.AzureAuthorityHosts;
import com.azure.identity.DefaultAzureCredentialBuilder;

import com.azure.resourcemanager.AzureResourceManager;

import com.azure.identity.ClientSecretCredential;
import com.azure.identity.ClientSecretCredentialBuilder;

import com.azure.storage.blob.*;

// BigID stuff
//import com.azure.storage.file.datalake.*;
//import com.azure.storage.file.datalake.models.*;
//import com.azure.storage.file.datalake.options.*;

// (c) 2023 BigID

public class App {

    /*  Authenticate with client secret.
            */
    public void createClientSecretCredential() {
        ClientSecretCredential clientSecretCredential = new ClientSecretCredentialBuilder()
                .clientId("<YOUR_CLIENT_ID>")
                .clientSecret("<YOUR_CLIENT_SECRET>")
                .tenantId("<YOUR_TENANT_ID>")
                .build();
    }
    public static void main(String[] args) {

        try {
            TokenCredential credential = new DefaultAzureCredentialBuilder()
                    .authorityHost(AzureAuthorityHosts.AZURE_PUBLIC_CLOUD)
                    .build();


            System.out.println("SN INFO - DefaultAzureCredentialBuilder....OK");
            // If you don't set the tenant ID and subscription ID via environment variables,
            // change to create the Azure profile with tenantId, subscriptionId, and Azure environment.
            AzureProfile profile = new AzureProfile(AzureEnvironment.AZURE);

            System.out.println("SN INFO - AzureProfile....OK");

            AzureResourceManager azureResourceManager = AzureResourceManager.configure()
                    .withLogLevel(HttpLogDetailLevel.BASIC)
                    .authenticate(credential, profile)
                    .withDefaultSubscription();

            System.out.println("SN INFO -azureResourceManager....OK");


            // example using com.azure.storage.file.datalake.DataLakeFileSystemClient

            // this uses blob use azure blob storage library is needed

 //           String accountName = storage.name();
 //           String accountKey = keys.get(0).value();
 //           String endpoint = endpoints.primary().blob();
            
 //           BlobServiceClient storageClient = new BlobServiceClientBuilder()
 //                   .endpoint(endpoint)
 //                   .credential(credential)
 //                   .buildClient();
            
 //           BlobContainerClient blobContainerClient = storageClient.getBlobContainerClient("stevetest");
 //           blobContainerClient.create();

            // Write a blob to the container.
 //           String fileName = "helloazure.txt";
 //           String textNew = "Hello Azure";

 //           BlobClient blobClient = blobContainerClient.getBlobClient(fileName);
 //           InputStream is = new ByteArrayInputStream(textNew.getBytes());
 //           blobClient.upload(is, textNew.length());


            // ListFilesInDirectory();

        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
}
