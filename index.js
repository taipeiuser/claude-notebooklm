#!/usr/bin/env node
/**
 * claude-notebooklm
 * List and manage NotebookLM notebooks via the NotebookLM Enterprise API.
 *
 * Usage:
 *   node index.js list
 *
 * Required environment variables:
 *   GOOGLE_CLOUD_PROJECT   - Your GCP project number or ID
 *   NBLM_LOCATION          - API location (default: "global")
 *   NBLM_ENDPOINT_LOCATION - Endpoint location prefix (default: "global")
 *
 * Authentication (pick one):
 *   - Run `gcloud auth application-default login` before executing
 *   - Set GOOGLE_APPLICATION_CREDENTIALS to a service account key file
 *   - Set NBLM_ACCESS_TOKEN to a Bearer token
 */

import { GoogleAuth } from "google-auth-library";

const PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
const LOCATION = process.env.NBLM_LOCATION || "global";
const ENDPOINT_LOCATION = process.env.NBLM_ENDPOINT_LOCATION || "global";
const BASE_URL = `https://${ENDPOINT_LOCATION}-discoveryengine.googleapis.com`;

async function getAccessToken() {
  if (process.env.NBLM_ACCESS_TOKEN) {
    return process.env.NBLM_ACCESS_TOKEN;
  }
  const auth = new GoogleAuth({
    scopes: ["https://www.googleapis.com/auth/cloud-platform"],
  });
  const client = await auth.getClient();
  const tokenResponse = await client.getAccessToken();
  return tokenResponse.token;
}

async function listNotebooks() {
  if (!PROJECT) {
    console.error(
      "Error: GOOGLE_CLOUD_PROJECT environment variable is required.\n" +
        "Example: GOOGLE_CLOUD_PROJECT=123456789 node index.js list"
    );
    process.exit(1);
  }

  const token = await getAccessToken();
  const url =
    `${BASE_URL}/v1alpha/projects/${PROJECT}/locations/${LOCATION}` +
    `/notebooks:listRecentlyViewed`;

  const response = await fetch(url, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    const body = await response.text();
    console.error(`Error ${response.status}: ${response.statusText}`);
    console.error(body);
    process.exit(1);
  }

  const data = await response.json();
  const notebooks = data.notebooks || [];

  if (notebooks.length === 0) {
    console.log("No notebooks found.");
    return;
  }

  console.log(`Found ${notebooks.length} notebook(s):\n`);
  notebooks.forEach((nb, i) => {
    const name = nb.name || "";
    const id = name.split("/").pop();
    const title = nb.displayName || nb.title || "(untitled)";
    const updated = nb.updateTime
      ? new Date(nb.updateTime).toLocaleString()
      : "unknown";
    console.log(`${i + 1}. ${title}`);
    console.log(`   ID:      ${id}`);
    console.log(`   Updated: ${updated}`);
    if (nb.sourceCount !== undefined) {
      console.log(`   Sources: ${nb.sourceCount}`);
    }
    console.log();
  });
}

const command = process.argv[2] || "list";

switch (command) {
  case "list":
    listNotebooks().catch((err) => {
      console.error("Unexpected error:", err.message);
      process.exit(1);
    });
    break;
  default:
    console.error(`Unknown command: ${command}`);
    console.error("Available commands: list");
    process.exit(1);
}
