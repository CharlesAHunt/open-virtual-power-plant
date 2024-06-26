use axum::{response::Html, routing::get, Router};

#[tokio::main]
async fn main() {
    // build our application with a route
    let app = Router::new()
        .route("/", get(get_der))
        .route("/", post(create_der));

    // run it
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000")
        .await
        .unwrap();
    println!("listening on {}", listener.local_addr().unwrap());
    axum::serve(listener, app).await.unwrap();
}

async fn get_der(Path(user_id) : Path<Uuid>) -> Json<DER> {
    let der = find_der(user_id).await;
    Json(der)
}

async fn create_der(extract::Json(payload): extract::Json<DER>) {
    // payload is a `DER`
}