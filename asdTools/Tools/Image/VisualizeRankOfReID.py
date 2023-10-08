from asdTools.Classes.Tool.MarkdownTable import MarkdownTable
from asdTools.Classes.Base.BaseModel import BaseModel
import numpy as np

class VisualizeRankOfReID(BaseModel):
    """ Sample: Sample/VisualizeRankOfReID
    使用markdown表格进行ReID的Rank可视化。速度快，我的笔记本运行一次3543x3384(query-gallery)的可视化耗时9秒。
    Visualize ReID Rank by markdown tables. Fast - It takes only 9 seconds to generate visualizations on my laptop for a 3543x3384 query-gallery."
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(multipleFiles=True, **kwargs)

    def __call__(self, 
            distmat, 
            query_loader, 
            gallery_loader, 
            top_k:int=10,
            pid_index:int=1,
            camid_index:int=2) -> str:
        self.run(distmat, query_loader, gallery_loader, top_k, pid_index, camid_index)
        
    def run(self, 
            distmat, 
            query_loader, 
            gallery_loader, 
            top_k,
            pid_index,
            camid_index) -> str:
        self.begining(isSimple=True)
        if top_k == -1: 
            self.warning("top_k is set to -1, all images will be shown, may too large.")
            top_k = distmat.shape[0]
        index2path = ""
        # ---------- Init Guery Datainfo ----------
        g_imgs = []
        g_pids = []
        g_camids = []
        for i, data_info in enumerate(gallery_loader.dataset.dataset):
            g_imgs.append(data_info[0])
            g_pids.append(data_info[pid_index])
            g_camids.append(data_info[camid_index])
        # ---------- Start Visualazation ----------
        for i, data_info in enumerate(query_loader.dataset.dataset):
            # ---------- Init Query Datainfo ----------
            q_img_path = data_info[0]
            q_pid = data_info[pid_index]
            q_camid = data_info[camid_index]
            # ---------- Sort Rank ----------
            distances = distmat[i]
            sorted_indices = np.argsort(distances)
            sorted_indices = [index for index in sorted_indices if g_camids[index] != q_camid]
            sorted_indices = [index for index in sorted_indices if g_pids[index] != q_pid]
            # ---------- Save Rank ----------
            # ----- map i_query to img_path of i_query
            index2path += f"{i+1}: \t {self.convert_path_to_abspath(q_img_path)} \n"
            # ----- rank gallery of i_query
            # rank gallery imgs
            g_imgs_path = [g_imgs[index] for index in sorted_indices[:top_k]]
            # log imgs
            md_table = MarkdownTable(["i", "query"] + [f"top_{j+1}" for j in range(top_k)])
            row_imgs = [i + 1]
            row_imgs.append(md_table.convert_imgPath_to_MDImgPath(self.convert_path_to_abspath(q_img_path)))
            row_imgs.extend([md_table.convert_imgPath_to_MDImgPath(self.convert_path_to_abspath(g_imgs_path[j])) for j in range(top_k)])
            md_table.add_row(row_imgs)
            # log id
            row_ID = ["data info"]
            row_ID.append(data_info[1:])
            row_ID.extend([gallery_loader.dataset.dataset[j][1:] for j in sorted_indices[:top_k]])
            md_table.add_row(row_ID)
            # save markdown table
            md_table_path = self.generate_output_path(output_middle_dir=self._time_start, output_file=f"{i+1}-rank_table.md")
            self.save_file(md_table.output(), md_table_path)
        # ---------- Save Mapping ----------
        index2path_path = self.generate_output_path(output_middle_dir=self._time_start, output_file=f"0_index2path.txt")
        self.save_file(index2path, index2path_path)
        self.log(f"For find image faster, see mapping in {index2path_path}")
        self.done(isSimple=True)


if __name__ == "__main__":
    # All you need is place the codes before evaluate(distmat, ...) in test()
    
    # ---------- Sample 1 ----------
    """ When specify log_dir
    
def test_prcc(model, queryloader_same, queryloader_diff, galleryloader, dataset):
    logger = logging.getLogger('reid.test')
    ...

    from asdTools.Tools.Image.VisualizeRankOfReID import VisualizeRankOfReID
    rank_vis = VisualizeRankOfReID()
    log_dir = rank_vis.get_loggingLogger_path(logger)
    log_dir = rank_vis.join(log_dir, "Rank Visualization")
    VisualizeRankOfReID(log_dir=log_dir)(distmat, queryloader, galleryloader)
    
    logger.info("Computing CMC and mAP for the same clothes setting")
    cmc, mAP = evaluate(distmat_same, qs_pids, g_pids, qs_camids, g_camids)
    """

    # ---------- Sample 2 ----------
    """ Just visualization
    
def test_prcc(model, queryloader_same, queryloader_diff, galleryloader, dataset):

    from asdTools.Tools.Image.VisualizeRankOfReID import VisualizeRankOfReID
    VisualizeRankOfReID()(distmat, queryloader, galleryloader)
    
    logger.info("Computing CMC and mAP for the same clothes setting")
    cmc, mAP = evaluate(distmat_same, qs_pids, g_pids, qs_camids, g_camids)
    """
