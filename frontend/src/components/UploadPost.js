import { FileUpload } from 'primereact/fileupload';

export default function UploadPost() {
    const obj = {
        "user_id": 1,
        "title": "post_title",
        "description": "ala ma kota",
        "create_date": "2023-05-16",
        "image": "http://localhost:8000/images/githubFlow2.jpeg",
        "tags": [
            1
        ]
    }
    return (
        <UploadContainer>
            <FileUpload name="avatar"
                url={`http://localhost:8000/api/image/`}
                maxFileSize={1000000}
                accept={"image/*"}
                key={Date.now()}
                // onUpload={onUpload}
                // cancelLabel={t("kanbanChangeUserDataDialogCancel")}
                // uploadLabel={t("kanbanChangeUserDataDialogUpload")}
                // chooseLabel={t("kanbanChangeUserDataDialogChoose")}
                // emptyTemplate={emptyTemplate(t)}
                // invalidFileSizeMessageDetail={t("kanbanChangeUserDataDialogInvalidSizeMessageDetail")}
                // invalidFileSizeMessageSummary={t("kanbanChangeUserDataDialogInvalidSizeMessage")}
                mode={"advanced"}
            />
        </UploadContainer>
    );
}